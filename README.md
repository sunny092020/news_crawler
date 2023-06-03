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

start crawling by open another terminal (while keeping the above terminal running)
```
./script/start_spider.sh
```
after finish crawling, open browser to see articles
```
http://10.3.0.6:3000/
```

This is for educational and experimental purpose only.  
Use it with respect for the site owner.  

Thank you!