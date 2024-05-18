from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'core.my_cron_job'    # a unique code

    def do(self):
        print("run cron eve 1 minute")