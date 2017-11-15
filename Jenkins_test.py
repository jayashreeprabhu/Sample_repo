from jenkinsapi.jenkins import Jenkins
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

server = Jenkins('https://jenkins.onemw.net', username='jayashreeprabhu', password='d801d349b959cff99291ce53fec79b80', ssl_verify=False)

job_name = 'StbFullStackRegression'
# job_name = 'Deploy to Lab5A ITC shared Origin'
print "all jobs"

job_names_list = []
# for job_name, job_instance in server.get_jobs():
#         job_names_list.append(job_instance.name)

# if server.has_job(job_name):
#         job_instance = server.get_job(job_name)
#         print job_instance
#         print job_instance.is_running()
#         print job_instance.get_revision()

# job = server[job_name]

job = server.get_job(job_name)  # or j[JOB_NAME]
build = job.get_build(1070)
parameters = build.get_actions()['parameters']
meta = job.get_build_metadata(1070)
# result = build.get_resultset()
# x = build.get_env_vars()
x = build.get_env_vars()
print "========================="
print x
print "========================="


# for i in job_names_list:
#
#         print i

# print "server has job"
# print server.has_job(job_name)