from jenkinsapi.jenkins import Jenkins
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

server = Jenkins('https://jenkins.onemw.net', username='jayashreeprabhu', password='d801d349b959cff99291ce53fec79b80', ssl_verify=False)

# job_name = 'StbFullStackRegression'
job_name = 'STB_Tests/Sample'
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
# parameters = build.get_actions()['parameters']

job = server.get_job(job_name)  # or j[JOB_NAME]
curr = job.is_running()
number = job.get_last_buildnumber()
number = 
build = job.get_build(number)
up_name = build.get_upstream_job_name()
up_build = build.get_upstream_build()
meta = up_build.get_status()


print curr
print number
print build
print up_name
print up_build
print meta




# for i in job_names_list:
#
#         print i

# print "server has job"
# print server.has_job(job_name)
