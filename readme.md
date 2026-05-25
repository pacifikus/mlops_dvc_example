## MLOps DVC Example

### Начало работы

Инициализируем git-репозиторий: `git init`

Инициализируем DVC: `dvc init`

### Настраиваем DVC-конфиг для работы с s3:

1. Добавляем бакет:
`dvc remote add -d minio_storage s3://test1`

2. Настраиваем использование ssl:
`dvc remote modify minio_storage use_ssl false`

3. Добавляем ссылку на minio:
`dvc remote modify minio_storage endpointurl http://85.239.47.84:9000`

Пример содержимого config-файла:
```
[core]
    remote = minio_storage
['remote "minio_storage"']
    url = s3://test1
    use_ssl = false
    endpointurl = http://85.239.47.84:9000
```

4. Потом добавьте credentials для minio в config.local


### Работа с DVC & GIT

1. Добавляем данные в DVC:
`dvc add <FILE/FOLDER NAME>`

2. Добавляем метаданные в git:
`git add <*.dvc FILE>`

3. Пушим данные через DVC в remote:
`dvc push`

4. Дальше все коммитим/пушим в git как обычно. 

...

5. Получаем данные через DVC из remote:
`dvc pull`

Или запускаем `dvc repro` для запуска пайплайна


