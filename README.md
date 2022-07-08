# Создание Dataset`ов 
1. Запустить файл main.py
2. При запуске указать:
   *  путь для сохранения папки DATASET
   *  путь к файлу содержащему фразу и название аудио файла
   *  путь к ауидо файлам
3. После завершения в указаном месте создастся папка DATASET, которая будет содержать подразделы с аудио файлами
   - <img width="160" alt="image" src="https://user-images.githubusercontent.com/91955445/177977978-ee98547f-63d6-4284-b257-3edfd4fbc105.png">

# Обучение нейронной сети
### Открыть файл .ipynb в [Google Colab](https://colab.research.google.com/)
1. Открыть вкладку менджмента папок
2. ПКМ по пустому пространству
   * <img width="387" alt="some" src="https://user-images.githubusercontent.com/91955445/177967673-4c48615c-f44e-4a33-8308-e1fb2d30abcd.png">
3. Загрузить папку с обучающими файлами
   - <img width="88" alt="image" src="https://user-images.githubusercontent.com/91955445/177975095-aad6c567-ecf0-4cc4-badf-638b131a382b.png">
   - Папка должна быть разделена на подразделы по словам
   - <img width="104" alt="image" src="https://user-images.githubusercontent.com/91955445/177975210-156e8428-c17a-4f88-b121-5ca885eb85c5.png">
   - Каждый раздел содержит .wav файлы
   - <img width="87" alt="image" src="https://user-images.githubusercontent.com/91955445/177975353-75dc9687-f2c3-45b9-bc01-7c8d5015965f.png">
   
* В переменную DATASET_PATH записать путь к загруженной папке
* В переменную model_path записать путь для сохранения файлов модели
  * <img width="253" alt="image" src="https://user-images.githubusercontent.com/91955445/177973093-d5f1e162-d618-418d-a53f-dd11628d5626.png">
* При необходимости перезаписать частоту аудио файла (По умолчанию 8000)
  * <img width="89" alt="image" src="https://user-images.githubusercontent.com/91955445/177973507-e0335c10-5ba7-4068-9f09-2565f355dd3f.png">
* При необходимости изменить количество эпох для обучения нейронной сети (По умолчанию 6)
  * <img width="82" alt="image" src="https://user-images.githubusercontent.com/91955445/177974221-7d8e9ef3-3f7a-4888-bed5-815c258295b6.png">

## По завершению работы программы необходимо скачать следующие файлы: 
 * Папка, содержащая модель (см. пример:)
    * <img width="81" alt="image" src="https://user-images.githubusercontent.com/91955445/177978109-fa04a6f3-c8d3-4610-99c2-f7b7da4eccb1.png">
    * <img width="130" alt="image" src="https://user-images.githubusercontent.com/91955445/177978089-cac52e84-6955-44ff-83ee-4ece16151ed5.png">
 * commands.txt (см. пример:)
    * <img width="121" alt="image" src="https://user-images.githubusercontent.com/91955445/177974053-05fb5909-6a9e-4d44-a95c-f3350a1bea67.png">
 




