-Use scrapy to navigate websites and extract data  
-Use Django, a high-level Python web framework, to manage and display the processed data and reactjs for frontend display.   
-To ensure the seamless handling of tasks and maintain high performance, integrate Celery, an asynchronous task queue/job queue  
-All the collected data is stored in PostgreSQL


install docker
```
sudo ./scripts/install_env.sh
```
build docker images
```
./scripts/build.sh
```

migrate db
```
./scripts/migrate.sh
```

create some categories to start manual testing
```
./script/init_data.sh
```

start the app
```
./scripts/start.sh
```

start crawling by open 2 another terminals (while keeping the above terminal running)  
each run a script
```
./script/start_dantri.sh
./script/start_vnexpress.sh
```
after finish crawling, open browser to see articles
```
http://10.3.0.6:3000/
```

This is for educational and experimental purpose only.  
Use it with respect for the site owner.  

Thanks and best regards!