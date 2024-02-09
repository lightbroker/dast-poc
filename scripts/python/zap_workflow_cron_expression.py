import random
import re
from zap_workflow_constants import ZapWorkflowConstants


class ZapWorkflowCronExpression:

    def __init__(self, existing_expressions=None):
        self.existing_expressions = existing_expressions if isinstance(existing_expressions, list) else None
        self.cron_pattern = '[0-9\\*][ ][0-9\\*][ ][0-9\\*][ ][0-9\\*][ ][0-9\\*]'
        self.constants = ZapWorkflowConstants()
        self.possible_minute_intervals = [ 0, 15, 30, 45 ]
        self.possible_hours = range(self.constants.SCHEDULE_MIN_HOUR_UTC, self.constants.SCHEDULE_MAX_HOUR_UTC)
        self.possible_days = range(1, self.constants.SCHEDULE_MAX_DAY)
        self.reserved = []
        self._enumerate_existing()


    def _enumerate_existing(self):
        """
            Validates cron string items within `self.existing_expressions`,
            and defines `self.reserved` list.
        """

        if self.existing_expressions is None:
            self.reserved = []
            return

        for cron in self.existing_expressions:
            if re.search(self.cron_pattern, cron) == None:
                continue

            m = cron[0]
            h = cron[2]
            d = cron[4]

            if not (m.isdigit() and h.isdigit() and d.isdigit()):
                continue

            self.reserved.append([ m,h,d ])


    def _generate_candidate(self):
        return [ 
            random.choice(self.possible_minute_intervals),
            random.choice(self.possible_hours),
            random.choice(self.possible_days)
        ]


    def create(self, constrain=True):
        """
            Create a cron expression that does not match any existing expression, 
            or return default expression if `constrain` is `False` 
        """
        if constrain == False:
            return '0 0 1 * *'
        
        candidate = self._generate_candidate()

        while (candidate in self.reserved):
            candidate = self._generate_candidate()
        else:
            cron = f'{candidate[0]} {candidate[1]} {candidate[2]} * *'
            print(cron)
            return cron
