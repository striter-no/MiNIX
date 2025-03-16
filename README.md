# MiNIX

Расшифровывается как Mind UNIX. Проект является PoC (Proof of Concept) для создания виртуальной линукс машины с помощью `GPT`

## Принцип работы

1. Пользователь вводит запрос, который является собой консольной командой Linux
2. Выбранная модель `GPT` обрабатывает данный запрос и выводит предсказанный вывод этой команды в терминал

## Пример

```shell
$ ls
Desktop  Documents  Downloads  Music  Pictures  Videos
```

## Как запустить

```shell
pip install -r ./reqs.txt
python ./linux.py
```

Выход - `Ctrl + C`

