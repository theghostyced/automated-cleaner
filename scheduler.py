from logger import Logger

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
        self.logger = Logger()

    def run_daily(self, task: str):
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

        self.schedule.every().day.do(task).tag(tag)

        self.logger.write(f'Run job {tag} daily.')
        return self

    def run_daily_at_time(self, task: str, time: str):
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

        self.logger.write(f'Run job {tag} daily at {time} time')
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
            self.logger.write('Starting up all jobs')
            self.schedule.run_pending()

    def clear_jobs(self, tag: str | bool=None):
        """
        Description
        -----------
            Clears the job(s) with the given task else it clears all
            jobs

        Parameters
        ----------
            tag : str | bool
                Tag identifier for a job

        Returns
        -------
        None
        """

        self.logger.write('Clearing all jobs') if not tag else self.logger.write(f'Clearing {tag} job')
        self.schedule.clear(tag)
