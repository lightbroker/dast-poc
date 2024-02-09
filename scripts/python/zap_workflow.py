'''
    Represents a GitHub Action Worflow leveraging ZAP DAST scanning
    Author: Adam Wilson (https://github.com/lightbroker)

    Usage:
        python zap_workflow.py -t 'example.hostname.com' -d './../..' 

    Given a supplied hostname, generates:
        1.) YAML workflow for GitHub Actions
        2.) Default ruleset
        3.) Default context

'''

import argparse
import json
from zap_workflow_constants import ZapWorkflowConstants
from zap_workflow_cron_expression import ZapWorkflowCronExpression


class ZapWorkflow:

    def __init__(self, target_hostname, base_directory):
        self.constants = ZapWorkflowConstants()
        self.target_hostname = target_hostname
        self.schedule_file = f'{base_directory}/schedule.json'
        self.ruleset_template_file = f'{base_directory}/templates/rules.tsv'
        self.workflow_template_file = f'{base_directory}/templates/workflow.yml.txt'
        self.rulesets_path = f'{base_directory}/rules'
        self.workflows_path = f'{base_directory}/.github/workflows'


    def _load_template(self, file_path):
        try: 
            with open(file_path, 'r') as f:
                template = f.read()
                return template
            
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")


    def _load_schedule(self):
        try:
            with open(self.schedule_file, 'r') as file:
                data = json.load(file)
                return data

        except FileNotFoundError:
            print(f"Error: File not found - {self.schedule_file}")
        except json.JSONDecodeError:
            print(f"Error: Unable to decode JSON in the file - {self.schedule_file}")


    def _generate_cron(self):
        schedule_json = self._load_schedule()
        unavailable_times = list(schedule_json.values())
        cron_expression = ZapWorkflowCronExpression(unavailable_times)
        return cron_expression.create()


    def _update_schedule(self, key, value):
        try:
            data = self._load_schedule()

            if key not in data:
                data[key] = value
                with open(self.schedule_file, 'w') as file:
                    json.dump(data, file, indent=2)

                print(f"Entry added successfully: \"{key}\": \"{value}\"")
            else:
                print(f"Key already exists: \"{key}\"")

        except FileNotFoundError:
            print(f"Error: File not found - {self.schedule_file}")
        except json.JSONDecodeError:
            print(f"Error: Unable to decode JSON in the file - {self.schedule_file}")


    def _write(self, text, file_path):
        try:
            with open(file_path, 'w') as file:
                file.write(text)
            print(f"Text written to \"{file_path}\" successfully.")
        except Exception as e:
            print(f"Error: {e}")


    def create(self):
        # create cron expression
        cron = self._generate_cron()
        
        # get YAML template, replace string tokens
        workflow = self._load_template(self.workflow_template_file)
        workflow = workflow.replace(self.constants.TOKEN_CRON_SCHEDULE, cron)
        workflow = workflow.replace(self.constants.TOKEN_TARGET_HOSTNAME, self.target_hostname)
        # write YAML worflow
        self._write(workflow, f'{self.workflows_path}/dast_workflow.{self.target_hostname}.yml')
        
        # update schedule
        self._update_schedule(f'https://{self.target_hostname}', cron)

        # TODO get context template, replace string tokens
        # write base context
        
        # get ruleset template
        # write base ruleset
        ruleset = self._load_template(self.ruleset_template_file)
        self._write(ruleset, f'{self.rulesets_path}/rules.{self.target_hostname}.tsv')


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', dest='target', help='Target hostname')

    parser.add_argument('-d', dest='dir', help='Path to base directory')
    args = parser.parse_args()
    
    workflow = ZapWorkflow(args.target, args.dir)
    workflow.create()
