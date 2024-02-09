import unittest
from zap_workflow import ZapWorkflow
from zap_workflow_cron_expression import ZapWorkflowCronExpression

class ZapWorkflowUnitTests(unittest.TestCase):

    def test_returns_unique_cron_expression(self):
        reserved = [
            '0 1 7 * *',
            '0 1 12 * *',
            '15 5 1 * *'
        ]
        cron = ZapWorkflowCronExpression(reserved)
        expression = cron.create()
        print(f'test_returns_unique_cron_expression: {expression}')
        self.assertIsNotNone(expression)
        self.assertIsNotNone('expression')
        self.assertFalse(expression in reserved)

    def test_returns_unique_cron_expression2(self):
        reserved = [
            '0 9 7 * *',
            '0 3 12 * *',
            '45 10 3 * *'
        ]
        cron = ZapWorkflowCronExpression(reserved)
        expression = cron.create()
        print(f'test_returns_unique_cron_expression2: {expression}')
        self.assertIsNotNone(expression)
        self.assertIsNotNone('expression')
        self.assertFalse(expression in reserved)

    def test_returns_cron_expression(self):
        cron = ZapWorkflowCronExpression()
        expression = cron.create()
        print(f'3: {expression}')
        self.assertIsNotNone(expression)


if __name__ == '__main__':
    unittest.main()
