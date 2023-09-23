# hotel_booking
Stepik course. Hotel booking project using FastApi


isort
```bash
isort app/rooms/router.py -m=3 --tc
```

yapf
```bash
yapf --style=linters/.style.yapf \
    --parallel \
    --in-place \
    --recursive \
    --verbose \
    app/
```

pyright 
```bash
 pyright -p linters/pyrightconfig.json app
```

bandit
```bash
 bandit -c linters/bandit.yaml -r app/
```