import schedule
import datetime


class Scheduler:
    """
    Description
    -----------
        Takes care of setting up cron job

    Attributes
    ----------
        cron
            holds our CronTab instance
    """

    def __init__(self):
        """
        Description
        -----------
            Initializes our crontab instance
        """
        self.schedule = schedule
        self.schedule_tag = 'job'

    def run_daily(self, task):
        """
        Descritpion
        -----------
            Sets up a daily cron job

        Parameters
        ----------
            task : str
                Script we want executed daily

        Returns
        -------
            self : Scheduler Instance
                Returns the scheduler instance
        """

        tag = f'{self.schedule_tag}_{datetime.datetime.now()}'

        job = self.schedule.every().day.do(task).tag(tag)

        # Log invoked job here
        return self

    def run_daily_at_time(self, task, time):
        """
        Descritpion
        -----------
            Sets up a daily cron job

        Parameters
        ----------
            task : str
                Script we want executed daily

            time : str
                Time of the day the script should run

        Returns
        -------
            self : Scheduler Instance
                Returns the scheduler instance
        """

        tag = f'{self.schedule_tag}_{datetime.datetime.now()}'

        self.schedule.every().day.at(time).do(task).tag(tag)
        return self

    def run_every_minute(self, task):
        """
        Descritpion
        -----------
            Run the task every minute

        Parameters
        ----------
            task : str
                Script we want executed daily

        Returns
        -------
            self : Scheduler Instance
                Returns the scheduler instance
        """

        tag = f'{self.schedule_tag}_{datetime.datetime.now()}'

        self.schedule.every().minute.do(task).tag(tag)
        return self

    def start(self):
        """
        Description
        -----------
            Begins the scheduled job

        Returns
        -------
            None
        """

        while True:
            self.schedule.run_pending()

    def clear_jobs(self, tag=None):
        """
        Description
        -----------
            Clears the job(s) with the given task else it clears all
            jobs

        Parameters
        ----------
            tag : str
                Tag identifier for a job

        Returns
        -------
        None
        """

        self.schedule.clear(tag)
