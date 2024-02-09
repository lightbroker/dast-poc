class ZapWorkflowConstants:
    def __init__(self):
        pass

    # string tokenization
    TOKEN_CRON_SCHEDULE =       '$$$CRON_SCHEDULE$$$'
    TOKEN_TARGET_HOSTNAME =     '$$TARGET_HOSTNAME$$$'
    
    # schedule constants
    SCHEDULE_MAX_DAY =          28
    SCHEDULE_MIN_HOUR_UTC =     1   # 7PM US Central Time / 1AM UTC 
    SCHEDULE_MAX_HOUR_UTC =     9   # 3AM US Central Time / 9AM UTC 
