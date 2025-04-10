-- Включение поддержки внешних ключей
PRAGMA foreign_keys = ON;

CREATE TABLE Users (
-- Таблица пользователей системы

    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_number TEXT NOT NULL UNIQUE, -- Уникальный номер пользователя
    abbreviation TEXT NOT NULL, -- Аббревиатура пользователя
    
    -- Проверки
    CHECK(length(user_number) > 0),
    CHECK(length(abbreviation) > 0)
);

CREATE TABLE Departments (
-- Таблица подразделений инициатора

    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE -- Название подразделения
);

CREATE TABLE Initiators (
-- Таблица инициаторов заданий

    initiator_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT NOT NULL, -- ФИО сотрудника
    feedback_number TEXT, -- Номер для обратной связи
    department_id INTEGER NOT NULL, -- Подразделение
    
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

CREATE TABLE Themes (
-- Таблица тематик заданий

    theme_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL UNIQUE -- Описание тематики
);

CREATE TABLE Topics (
-- Таблица тем

    topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL UNIQUE -- Описание темы

);

CREATE TABLE TaskTypes (
-- Таблица типов заданий

    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE, -- Название типа задания
    description TEXT -- Описание типа
);

CREATE TABLE Tasks (
-- Таблица заданий

    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_number TEXT NOT NULL UNIQUE, -- Номер задания
    start_date DATE NOT NULL, -- Дата создания
    end_date DATE, -- Дата создания
    comment TEXT, -- Комментарий к заданию
    executor_id INTEGER NOT NULL, -- Исполнитель
    initiator_id INTEGER NOT NULL, -- Инициатор
    type_id INTEGER NOT NULL, -- Тип задания
    theme_id INTEGER, -- Тема задания
    
    FOREIGN KEY (executor_id) REFERENCES Users(user_id),
    FOREIGN KEY (initiator_id) REFERENCES Initiators(initiator_id),
    FOREIGN KEY (type_id) REFERENCES TaskTypes(type_id),
    FOREIGN KEY (theme_id) REFERENCES Themes(theme_id)
);

CREATE TABLE Countries (
-- Таблица стран

    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE -- Название страны
);

CREATE TABLE Regions (
-- Таблица субъектов (регионов)

    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, -- Название региона
    country_id INTEGER NOT NULL, -- Страна
    
    FOREIGN KEY (country_id) REFERENCES Countries(country_id),
    UNIQUE(name, country_id)
);

CREATE TABLE Cities (
-- Таблица населенных пунктов

    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, -- Название населенного пункта
    region_id INTEGER NOT NULL, -- Регион
    country_id INTEGER NOT NULL, -- Страна
    
    FOREIGN KEY (region_id) REFERENCES Regions(region_id),
    FOREIGN KEY (country_id) REFERENCES Countries(country_id),
    UNIQUE(name, region_id)
);

CREATE TABLE Persons (
-- Таблица персон (физических лиц)

    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT NOT NULL, -- Фамилия
    first_name TEXT NOT NULL, -- Имя
    middle_name TEXT, -- Отчество
    birth_date DATE, -- Дата рождения
    birth_place_id INTEGER, -- Место рождения
    comment TEXT, -- Комментарий
    topic_id INTEGER,  -- Тематика

    FOREIGN KEY (topic_id) REFERENCES Topics(topic_id),
    FOREIGN KEY (birth_place_id) REFERENCES Cities(city_id),
    CHECK(length(last_name) > 0),
    CHECK(length(first_name) > 0)
);

CREATE TABLE PassportOffices (
-- Таблица паспортных столов

    office_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, -- Название паспортного стола
    department_code TEXT NOT NULL, -- Код подразделения
    country_id INTEGER NOT NULL, -- Страна
    
    FOREIGN KEY (country_id) REFERENCES Countries(country_id)
);

CREATE TABLE Passports (
-- Таблица паспортов

    passport_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL, -- Страна выдачи
    number_series TEXT NOT NULL, -- Серия и номер
    issue_date DATE, -- Дата выдачи
    issue_place_id INTEGER, -- Место выдачи (паспортный стол)
    person_id INTEGER NOT NULL, -- Владелец
    
    FOREIGN KEY (country_id) REFERENCES Countries(country_id),
    FOREIGN KEY (issue_place_id) REFERENCES PassportOffices(office_id),
    FOREIGN KEY (person_id) REFERENCES Persons(person_id),
    UNIQUE(number_series, country_id)
);

CREATE TABLE DriverLicenses (
-- Таблица водительских удостоверений

    license_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER NOT NULL, -- Страна выдачи
    region_id INTEGER NOT NULL, -- Регион выдачи
    number_series TEXT NOT NULL, -- Номер удостоверения
    issue_date DATE, -- Дата выдачи
    person_id INTEGER NOT NULL, -- Владелец
    
    FOREIGN KEY (country_id) REFERENCES Countries(country_id),
    FOREIGN KEY (region_id) REFERENCES Regions(region_id),
    FOREIGN KEY (person_id) REFERENCES Persons(person_id)
);

CREATE TABLE GovIdTypes (
-- Таблица типов гос. идентификаторов

    gov_id_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE -- Название типа идентификатора
);

CREATE TABLE GovIds (
-- Таблица гос. идентификаторов

    gov_id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL, -- Номер документа
    type_id INTEGER NOT NULL, -- Тип документа
    person_id INTEGER NOT NULL, -- Владелец
    
    FOREIGN KEY (type_id) REFERENCES GovIdTypes(gov_id_type_id),
    FOREIGN KEY (person_id) REFERENCES Persons(person_id),
    UNIQUE(number, type_id)
);

CREATE TABLE WorkHistory (
-- Таблица истории трудовой деятельности

    work_id INTEGER PRIMARY KEY AUTOINCREMENT,
    organization TEXT NOT NULL, -- Организация
    position TEXT NOT NULL, -- Должность
    start_date DATE NOT NULL, -- Дата начала
    end_date DATE, -- Дата окончания
    person_id INTEGER NOT NULL, -- Сотрудник
    
    FOREIGN KEY (person_id) REFERENCES Persons(person_id)
);

CREATE TABLE Locations (
-- Таблица мест пребывания

    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER NOT NULL, -- Населенный пункт
    address TEXT NOT NULL, -- Адрес
    
    FOREIGN KEY (city_id) REFERENCES Cities(city_id)
);

CREATE TABLE Violations (
-- Таблица правонарушений

    violation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL, -- Описание правонарушения
    person_id INTEGER NOT NULL, -- Нарушитель
    
    FOREIGN KEY (person_id) REFERENCES Persons(person_id)
);

CREATE TABLE Cars (
-- Таблица автомобилей

    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_plate TEXT, -- Гос. номер
    make TEXT, -- Марка
    color TEXT, -- Цвет
    pts_number TEXT, -- Номер ПТС
    sts_number TEXT, -- Номер СТС
    vin TEXT, -- VIN-номер
    person_id INTEGER NOT NULL, -- Владелец
    
    FOREIGN KEY (person_id) REFERENCES Persons(person_id),
    UNIQUE(vin)
);

CREATE TABLE TelecomOperators (
-- Таблица операторов связи

    operator_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE -- Название оператора
);

CREATE TABLE PhoneNumbers (
-- Таблица абонентских номеров

    phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL UNIQUE, -- Номер телефона
    operator_id INTEGER NOT NULL, -- Оператор
    region_id INTEGER, -- Регион регистрации
    topic_id INTEGER,  -- Тематика
    
    FOREIGN KEY (operator_id) REFERENCES TelecomOperators(operator_id),
    FOREIGN KEY (region_id) REFERENCES Regions(region_id),
    FOREIGN KEY (topic_id) REFERENCES Topics(topic_id)
);

CREATE TABLE PhonebookNames (
-- Таблица имен в телефонной книге

    name_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, -- Имя контакта
    phone_id INTEGER NOT NULL, -- Номер телефона
    
    FOREIGN KEY (phone_id) REFERENCES PhoneNumbers(phone_id)
);

CREATE TABLE ImsiNumbers (
-- Таблица IMSI

    imsi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL UNIQUE, -- IMSI номер
    start_date DATE, -- Дата начала
    end_date DATE, -- Дата окончания
    phone_id INTEGER NOT NULL, -- Привязанный номер
    
    FOREIGN KEY (phone_id) REFERENCES PhoneNumbers(phone_id)
);

CREATE TABLE ImeiNumbers (
-- Таблица IMEI

    imei_id INTEGER PRIMARY KEY AUTOINCREMENT,
    number TEXT NOT NULL UNIQUE -- IMEI номер
);

CREATE TABLE Emails (
-- Таблица email-адресов

    email_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE, -- Адрес электронной почты
    password TEXT, -- Пароль
    person_id INTEGER, -- Владелец
    topic_id INTEGER,  -- Тематика
    
    FOREIGN KEY (person_id) REFERENCES Persons(person_id),
    FOREIGN KEY (topic_id) REFERENCES Topics(topic_id)
);

CREATE TABLE Credentials (
-- Таблица учетных данных

    credential_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL, -- Логин
    password TEXT, -- Пароль
    description TEXT, -- Описание
    person_id INTEGER NOT NULL, -- Владелец
    
    FOREIGN KEY (person_id) REFERENCES Persons(person_id),
    UNIQUE(username)
);

CREATE TABLE InternetServices (
-- Таблица интернет-сервисов

    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE -- Название сервиса
);

CREATE TABLE Images (
-- Таблица изображений

    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    file BLOB, -- Бинарные данные изображения
    description TEXT -- Описание изображения
);

CREATE TABLE InternetAccounts (
-- Таблица аккаунтов в интернет-сервисах

    internet_accounts_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER NOT NULL, -- Сервис
    account_id TEXT NOT NULL, -- ID аккаунта
    username TEXT, -- Логин
    first_name TEXT, -- Имя
    last_name TEXT, -- Фамилия
    last_online_date DATETIME, -- Дата последнего входа
    registration_date DATE, -- Дата регистрации
    birth_date DATE, -- Дата рождения
    city_id INTEGER, -- Населенный пункт
    has_profile_image BOOLEAN, -- Наличие аватарки
    profile_image_id INTEGER, -- Аватарка
    has_personal_photos BOOLEAN, -- Наличие личных фото
    personal_photos_description TEXT, -- Описание фото
    profile_url TEXT, -- URL профиля
    screenshot_id INTEGER, -- Скриншот профиля
    is_private BOOLEAN, -- Приватность профиля
    comment TEXT, -- Комментарий
    person_id INTEGER NOT NULL, -- Владелец аккаунта
    topic_id INTEGER,  -- Тематика
    
    FOREIGN KEY (service_id) REFERENCES InternetServices(service_id),
    FOREIGN KEY (city_id) REFERENCES Cities(city_id),
    FOREIGN KEY (profile_image_id) REFERENCES Images(image_id),
    FOREIGN KEY (screenshot_id) REFERENCES Images(image_id),
    FOREIGN KEY (person_id) REFERENCES Persons(person_id),
    FOREIGN KEY (topic_id) REFERENCES Topics(topic_id),
    UNIQUE(service_id, account_id)
);

CREATE TABLE WebPages (
-- Таблица интернет-страниц

    page_id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL UNIQUE, -- URL страницы
    screenshot_id INTEGER, -- Скриншот страницы
    description TEXT, -- Описание
    person_id INTEGER NOT NULL, -- Владелец
    
    FOREIGN KEY (screenshot_id) REFERENCES Images(image_id),
    FOREIGN KEY (person_id) REFERENCES Persons(person_id)
);

CREATE TABLE CommunityThemes (
-- Таблица тематик интернет-сообществ
    theme_id INTEGER PRIMARY KEY AUTOINCREMENT,
    theme_name TEXT NOT NULL UNIQUE,  -- Название тематики
    description TEXT                 -- Описание
);

CREATE TABLE OnlineCommunities (
-- Таблица интернет-сообществ

    online_communities_id INTEGER PRIMARY KEY AUTOINCREMENT,
    communities_id TEXT NOT NULL, -- ID интернет-сообщества
    has_profile_image BOOLEAN, -- Наличие аватарки
    profile_image_id INTEGER, -- Аватарка
    url TEXT, -- URL сообщества
    screenshot_id INTEGER, -- Скриншот сообщества
    description TEXT, -- Описание
    service_id INTEGER NOT NULL, -- Сервис
    theme_id INTEGER,

    FOREIGN KEY (profile_image_id) REFERENCES Images(image_id),
    FOREIGN KEY (screenshot_id) REFERENCES Images(image_id),
    FOREIGN KEY (theme_id) REFERENCES CommunityThemes(theme_id),
    FOREIGN KEY (service_id) REFERENCES InternetServices(service_id),
    UNIQUE(service_id, communities_id)
);


CREATE TABLE AddressTypes (
-- Таблица типов адресов (регистрация, проживание и т.п.)

    address_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE -- Название типа адреса
);

CREATE TABLE PersonRelationTypes (
-- Таблица типов связей между персонами

    relation_type_id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE -- Название типа связи
);

CREATE TABLE AccountRelationTypes (
-- Таблица типов связей между аккаунтами

    relation_type_id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE -- Название типа связи
);

CREATE TABLE DataBaseVersion (
-- Таблица версия базы данных
    data_base_version_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER NOT NULL, -- Версия
    date DATE, -- Дата
    comment TEXT -- Комментарий к версии
);

-- ===================== СВЯЗУЮЩИЕ ТАБЛИЦЫ =====================

CREATE TABLE TaskPersons (
-- Связь заданий и персон

    task_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    
    PRIMARY KEY (task_id, person_id),
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id),
    FOREIGN KEY (person_id) REFERENCES Persons(person_id)
);

CREATE TABLE TaskPhoneNumbers (
-- Связь заданий и абонентских номеров

    task_id INTEGER NOT NULL,
    phone_id INTEGER NOT NULL,
    
    PRIMARY KEY (task_id, phone_id),
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id),
    FOREIGN KEY (phone_id) REFERENCES PhoneNumbers(phone_id)
);

CREATE TABLE TaskInternetAccounts (
-- Связь заданий и аккаунтов

    task_id INTEGER NOT NULL,
    internet_accounts_id INTEGER NOT NULL,
    
    PRIMARY KEY (task_id, internet_accounts_id),
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id),
    FOREIGN KEY (internet_accounts_id) REFERENCES InternetAccounts(internet_accounts_id)
);

CREATE TABLE TaskEmails (
-- Связь заданий и email-адресов

    task_id INTEGER NOT NULL,
    email_id INTEGER NOT NULL,
    
    PRIMARY KEY (task_id, email_id),
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id),
    FOREIGN KEY (email_id) REFERENCES Emails(email_id)
);

CREATE TABLE PersonPhoneNumbers (
-- Связь абонентских номеров и персон

    person_id INTEGER NOT NULL,
    phone_id INTEGER NOT NULL,
    start_date DATE, -- Дата начала связи
    end_date DATE, -- Дата окончания связи
    
    PRIMARY KEY (person_id, phone_id),
    FOREIGN KEY (person_id) REFERENCES Persons(person_id),
    FOREIGN KEY (phone_id) REFERENCES PhoneNumbers(phone_id)
);

CREATE TABLE ImeiImsi (
-- Связь IMEI и IMSI

    imei_id INTEGER NOT NULL,
    imsi_id INTEGER NOT NULL,
    start_date DATE, -- Дата начала связи
    end_date DATE, -- Дата окончания связи
    
    PRIMARY KEY (imei_id, imsi_id),
    FOREIGN KEY (imei_id) REFERENCES ImeiNumbers(imei_id),
    FOREIGN KEY (imsi_id) REFERENCES ImsiNumbers(imsi_id)
);

CREATE TABLE CommunityMembers (
-- Связь интернет-сообществ и аккаунтов

    online_communities_id INTEGER NOT NULL,
    internet_accounts_id INTEGER NOT NULL,
    
    PRIMARY KEY (online_communities_id, internet_accounts_id),
    FOREIGN KEY (online_communities_id) REFERENCES OnlineCommunities(online_communities_id),
    FOREIGN KEY (internet_accounts_id) REFERENCES InternetAccounts(internet_accounts_id)
);

CREATE TABLE PersonLocations (
-- Связи между персонами и адресами

    person_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    address_type_id INTEGER NOT NULL, 
    
    PRIMARY KEY (person_id, location_id),
    FOREIGN KEY (person_id) REFERENCES Persons(person_id),
    FOREIGN KEY (location_id) REFERENCES Locations(location_id),
    FOREIGN KEY (address_type_id) REFERENCES AddressTypes(address_type_id)
);

CREATE TABLE PersonRelations (
-- Связи между персонами

    person1_id INTEGER NOT NULL,
    person2_id INTEGER NOT NULL,
    relation_type_id INTEGER NOT NULL,
    
    PRIMARY KEY (person1_id, person2_id),
    FOREIGN KEY (person1_id) REFERENCES Persons(person_id),
    FOREIGN KEY (person2_id) REFERENCES Persons(person_id),
    FOREIGN KEY (relation_type_id) REFERENCES PersonRelationTypes(relation_type_id),
    CHECK(person1_id < person2_id) -- Предотвращение дублирования связей
);

CREATE TABLE AccountRelations (
-- Связи между аккаунтами

    account1_id INTEGER NOT NULL,
    account2_id INTEGER NOT NULL,
    relation_type_id INTEGER NOT NULL,
    
    PRIMARY KEY (account1_id, account2_id),
    FOREIGN KEY (account1_id) REFERENCES InternetAccounts(internet_accounts_id),
    FOREIGN KEY (account2_id) REFERENCES InternetAccounts(internet_accounts_id),
    FOREIGN KEY (relation_type_id) REFERENCES AccountRelationTypes(relation_type_id),
    CHECK(account1_id < account2_id) -- Предотвращение дублирования связей
);