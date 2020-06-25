# Logstash Pipelines Monitor

Python Script to Monitor Logstash Pipelines

# Dependencies

    - Please check requirements.txt file to install all dependencies.
    - This script was developed to run on python3.7 or above due to f-strings.

# Configuration File

This script will check YAML configuration file config.yml to be able to iterate
over multiples logstash servers and pipelines.

You can easily configure a new logstash server and all pipelines.

    servers:
      logstash01:
        ip: 127.0.0.1
        port: 9600
        pipelines:
          - cisco
          - arista
          - mikrotik
      logstash02:
        ip: 127.0.0.1
        port: 9600
        pipelines:
          - cisco
          - arista
      logstash03:
        ip: 127.0.0.1
        port: 9600
        pipelines:
          - cisco
          - huawei

Ensure you have mapped all pipelines, and your script is able to reach logstash IP and Port.

# How to run the script

This script was built using Python OOB using class and methods so in this case you can run directly on the main script logstash_pipeline_mon.py:

  - Once instantiate the class, you must set config.yml file location.

        if __name__ == '__main__':

            connect = PipelineMon(config='config.yml')
            connect.get_logstash_data()

  - Run the script by:

  $ ./logstash_pipeline_mon.py

Or you can import this module on your own script.
