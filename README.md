toast38coza.djangoapp
=====================

Ansible role fo installing one or more django apps on a single server. Installs all requirements. 

### Install 

    ansible-galaxy install toast38coza.djangoapp
    

### Usage

**Example playbook:**

	- hosts: all
  
  	pre_tasks:
    	- name: update apt cache 
      	apt: update_cache=yes cache_valid_time=3600    

  	roles:
    	- toast38coza.djangoapp

 
  	vars:
    	postgresql_databases:
	      - name: ..

    	postgresql_users:
	      - name: ..
    	    pass: ..
        	encrypted: no       # denotes if the password is already encrypted.

	    postgresql_user_privileges:
    	  - name: projectservice          # user name
        	db: projectservice            # database
	        priv: "ALL"        # privilege string format: example: INSERT,UPDATE/table:SELECT/anothertable:ALL

    
    ## notes: path_to_requirements, path_to_managepy: unless blank, must have trailing slash
	    	django_apps: 
    	  - {
        	"djangoapp_projectname" : "..", 
	        "djangoapp_track_branch": "master", 
	        "djangoapp_repo" : "git@github.com:TangentMicroServices/...git", 
    	    "path_to_requirements" : "", 
        	"path_to_managepy" : "",
	        "djangoapp_httpport": 8005,
    	    "djangoapp_static" : true,
        	"djangoapp_domains" : "myapp.example.com",
	        "djangoapp_pythonversion" : "2.7",
    	    "djangoapp_db_engine" : "postgresql_psycopg2",
        	"djangoapp_db_host" : "127.0.0.1" }


**Run with:**

	ansible-playbook playbook.yml -i hosts -u username

