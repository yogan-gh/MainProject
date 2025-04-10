// Основные таблицы системы документооборота и учета персональных данных

Table Users {
  user_id integer [primary key, increment]
  user_number text [not null, unique]
  abbreviation text
  note: "Пользователи системы (исполнители заданий)"
}

Table Departments {
  department_id integer [primary key, increment]
  name text
  synonym text
  note: "Подразделения организации"
}

Table Employees {
  employee_id integer [primary key, increment]
  name text
  employee_number text [not null]
  synonym text
  department_id integer [not null]
  note: "Сотрудники организации"
}

Table TaskSubjects {
  subject_id integer [primary key, increment]
  name text [not null, unique]
  note: "Темы/предметы заданий"
}

Table Tasks {
  task_id integer [primary key, increment]
  start_date date [not null]
  end_date date
  user_id integer [not null]
  subject_id integer [not null]
  note: "Задания для сотрудников"
}

Table TaskRelationTypes {
  relation_type_id integer [primary key, increment]
  name text [not null, unique]
  note: "Типы связей между заданиями"
}

// Таблицы документооборота
Table IncomingTypes {
  type_id integer [primary key, increment]
  name text [not null, unique]
  note: "Типы входящих документов"
}

Table OutgoingTypes {
  type_id integer [primary key, increment]
  name text [not null, unique]
  note: "Типы исходящих документов"
}

Table Incoming {
  incoming_id integer [primary key, increment]
  date date [not null]
  reg_number text [not null]
  department_id integer [not null]
  employee_id integer [not null]
  type_id integer [not null]
  note: "Входящие документы"
  indexes {
    (date, reg_number) [unique]
  }
}

Table Outgoing {
  outgoing_id integer [primary key, increment]
  date date [not null]
  reg_number text [not null]
  department_id integer [not null]
  employee_id integer [not null]
  type_id integer [not null]
  note: "Исходящие документы"
  indexes {
    (date, reg_number) [unique]
  }
}

// Таблицы географических данных
Table Countries {
  country_id integer [primary key, increment]
  name text [not null, unique]
  note: "Страны"
}

Table Regions {
  region_id integer [primary key, increment]
  name text [not null]
  country_id integer [not null]
  note: "Регионы/субъекты"
  indexes {
    (name, country_id) [unique]
  }
}

Table Cities {
  city_id integer [primary key, increment]
  name text [not null]
  region_id integer [not null]
  country_id integer [not null]
  note: "Населенные пункты"
  indexes {
    (name, region_id) [unique]
  }
}

// Таблицы персональных данных
Table Topics {
  topic_id integer [primary key, increment]
  description text [not null, unique]
  note: "Темы для классификации персон"
}

Table Persons {
  person_id integer [primary key, increment]
  last_name text [not null]
  first_name text [not null]
  middle_name text
  birth_date date
  birth_place_id integer
  comment text
  topic_id integer
  note: "Физические лица (персоны)"
}

Table PassportOffices {
  office_id integer [primary key, increment]
  name text [not null]
  department_code text [not null]
  country_id integer [not null]
  note: "Паспортные столы"
}

Table Passports {
  passport_id integer [primary key, increment]
  country_id integer [not null]
  number_series text [not null]
  issue_date date
  issue_place_id integer
  person_id integer [not null]
  note: "Паспортные данные"
  indexes {
    (number_series, country_id) [unique]
  }
}

Table DriverLicenses {
  license_id integer [primary key, increment]
  country_id integer [not null]
  region_id integer [not null]
  number_series text [not null]
  issue_date date
  person_id integer [not null]
  note: "Водительские удостоверения"
}

Table GovIdTypes {
  gov_id_type_id integer [primary key, increment]
  name text [not null, unique]
  note: "Типы гос. идентификаторов"
}

Table GovIds {
  gov_id integer [primary key, increment]
  number text [not null]
  type_id integer [not null]
  person_id integer [not null]
  note: "Государственные идентификаторы"
  indexes {
    (number, type_id) [unique]
  }
}

Table WorkHistory {
  work_id integer [primary key, increment]
  organization text [not null]
  position text [not null]
  start_date date [not null]
  end_date date
  person_id integer [not null]
  note: "Трудовая деятельность"
}

Table Locations {
  location_id integer [primary key, increment]
  city_id integer [not null]
  address text [not null]
  note: "Места пребывания"
}

Table Violations {
  violation_id integer [primary key, increment]
  description text [not null]
  person_id integer [not null]
  note: "Правонарушения"
}

Table Cars {
  car_id integer [primary key, increment]
  license_plate text
  make text
  color text
  pts_number text
  sts_number text
  vin text [unique]
  person_id integer [not null]
  note: "Автомобили"
}

// Таблицы связи и интернет-активности
Table TelecomOperators {
  operator_id integer [primary key, increment]
  name text [not null, unique]
  note: "Операторы связи"
}

Table PhoneNumbers {
  phone_id integer [primary key, increment]
  number text [not null, unique]
  operator_id integer [not null]
  region_id integer
  topic_id integer
  note: "Телефонные номера"
}

Table PhonebookNames {
  name_id integer [primary key, increment]
  name text [not null]
  phone_id integer [not null]
  note: "Имена в телефонной книге"
}

Table ImsiNumbers {
  imsi_id integer [primary key, increment]
  number text [not null, unique]
  start_date date
  end_date date
  phone_id integer [not null]
  note: "IMSI номера SIM-карт"
}

Table ImeiNumbers {
  imei_id integer [primary key, increment]
  number text [not null, unique]
  note: "IMEI номера устройств"
}

Table Emails {
  email_id integer [primary key, increment]
  email text [not null, unique]
  password text
  person_id integer
  topic_id integer
  note: "Электронные почты"
}

Table Credentials {
  credential_id integer [primary key, increment]
  username text [not null, unique]
  password text
  description text
  person_id integer [not null]
  note: "Учетные данные"
}

Table InternetServices {
  service_id integer [primary key, increment]
  name text [not null, unique]
  note: "Интернет-сервисы"
}

Table Images {
  image_id integer [primary key, increment]
  file blob
  description text
  note: "Изображения и фотографии"
}

Table InternetAccounts {
  internet_accounts_id integer [primary key, increment]
  service_id integer [not null]
  account_id text [not null]
  username text
  first_name text
  last_name text
  last_online_date datetime
  registration_date date
  birth_date date
  city_id integer
  has_profile_image boolean
  profile_image_id integer
  has_personal_photos boolean
  personal_photos_description text
  profile_url text
  screenshot_id integer
  is_private boolean
  comment text
  person_id integer [not null]
  topic_id integer
  note: "Аккаунты в интернет-сервисах"
  indexes {
    (service_id, account_id) [unique]
  }
}

Table WebPages {
  page_id integer [primary key, increment]
  url text [not null, unique]
  screenshot_id integer
  description text
  person_id integer [not null]
  note: "Веб-страницы"
}

Table CommunityThemes {
  theme_id integer [primary key, increment]
  theme_name text [not null, unique]
  description text
  note: "Тематики интернет-сообществ"
}

Table OnlineCommunities {
  online_communities_id integer [primary key, increment]
  communities_id text [not null]
  has_profile_image boolean
  profile_image_id integer
  url text
  screenshot_id integer
  description text
  service_id integer [not null]
  theme_id integer
  note: "Интернет-сообщества"
  indexes {
    (service_id, communities_id) [unique]
  }
}

// Справочники типов
Table AddressTypes {
  address_type_id integer [primary key, increment]
  name text [not null, unique]
  note: "Типы адресов (регистрация, проживание)"
}

Table PersonRelationTypes {
  relation_type_id integer [primary key, increment]
  name text [not null, unique]
  note: "Типы связей между персонами"
}

Table AccountRelationTypes {
  relation_type_id integer [primary key, increment]
  name text [not null, unique]
  note: "Типы связей между аккаунтами"
}

Table DataBaseVersion {
  data_base_version_id integer [primary key, increment]
  version integer [not null]
  date date
  comment text
  note: "Версии базы данных"
}

// Связующие таблицы
Table IncomingOutgoing {
  incoming_id integer [not null]
  outgoing_id integer [not null]
  indexes {
    (incoming_id, outgoing_id)
  }
  note: "Связь входящих и исходящих документов"
}

Table IncomingTasks {
  incoming_id integer [not null]
  task_id integer [not null]
  indexes {
    (incoming_id, task_id)
  }
  note: "Связь входящих документов и заданий"
}

Table OutgoingTasks {
  outgoing_id integer [not null]
  task_id integer [not null]
  indexes {
    (outgoing_id, task_id)
  }
  note: "Связь исходящих документов и заданий"
}

Table TaskRelations {
  task1_id integer [not null]
  task2_id integer [not null]
  relation_type_id integer [not null]
  indexes {
    (task1_id, task2_id)
  }
  note: "Связи между заданиями"
}

Table TaskPersons {
  task_id integer [not null]
  person_id integer [not null]
  indexes {
    (task_id, person_id)
  }
  note: "Связь заданий и персон"
}

Table TaskPhoneNumbers {
  task_id integer [not null]
  phone_id integer [not null]
  indexes {
    (task_id, phone_id)
  }
  note: "Связь заданий и телефонных номеров"
}

Table TaskInternetAccounts {
  task_id integer [not null]
  internet_accounts_id integer [not null]
  indexes {
    (task_id, internet_accounts_id)
  }
  note: "Связь заданий и интернет-аккаунтов"
}

Table TaskEmails {
  task_id integer [not null]
  email_id integer [not null]
  indexes {
    (task_id, email_id)
  }
  note: "Связь заданий и email-адресов"
}

Table PersonPhoneNumbers {
  person_id integer [not null]
  phone_id integer [not null]
  start_date date
  end_date date
  indexes {
    (person_id, phone_id)
  }
  note: "Связь персон и телефонных номеров"
}

Table ImeiImsi {
  imei_id integer [not null]
  imsi_id integer [not null]
  start_date date
  end_date date
  indexes {
    (imei_id, imsi_id)
  }
  note: "Связь IMEI и IMSI"
}

Table CommunityMembers {
  online_communities_id integer [not null]
  internet_accounts_id integer [not null]
  indexes {
    (online_communities_id, internet_accounts_id)
  }
  note: "Участники интернет-сообществ"
}

Table PersonLocations {
  person_id integer [not null]
  location_id integer [not null]
  address_type_id integer [not null]
  indexes {
    (person_id, location_id)
  }
  note: "Связь персон и мест пребывания"
}

Table PersonRelations {
  person1_id integer [not null]
  person2_id integer [not null]
  relation_type_id integer [not null]
  indexes {
    (person1_id, person2_id)
  }
  note: "Связи между персонами"
}

Table AccountRelations {
  account1_id integer [not null]
  account2_id integer [not null]
  relation_type_id integer [not null]
  indexes {
    (account1_id, account2_id)
  }
  note: "Связи между интернет-аккаунтами"
}

// Основные связи между таблицами
Ref: Employees.department_id > Departments.department_id
Ref: Tasks.user_id > Users.user_id
Ref: Tasks.subject_id > TaskSubjects.subject_id
Ref: Incoming.department_id > Departments.department_id
Ref: Incoming.employee_id > Employees.employee_id
Ref: Incoming.type_id > IncomingTypes.type_id
Ref: Outgoing.department_id > Departments.department_id
Ref: Outgoing.employee_id > Employees.employee_id
Ref: Outgoing.type_id > OutgoingTypes.type_id
Ref: Regions.country_id > Countries.country_id
Ref: Cities.region_id > Regions.region_id
Ref: Cities.country_id > Countries.country_id
Ref: Persons.birth_place_id > Cities.city_id
Ref: Persons.topic_id > Topics.topic_id
Ref: PassportOffices.country_id > Countries.country_id
Ref: Passports.country_id > Countries.country_id
Ref: Passports.issue_place_id > PassportOffices.office_id
Ref: Passports.person_id > Persons.person_id
Ref: DriverLicenses.country_id > Countries.country_id
Ref: DriverLicenses.region_id > Regions.region_id
Ref: DriverLicenses.person_id > Persons.person_id
Ref: GovIds.type_id > GovIdTypes.gov_id_type_id
Ref: GovIds.person_id > Persons.person_id
Ref: WorkHistory.person_id > Persons.person_id
Ref: Locations.city_id > Cities.city_id
Ref: Violations.person_id > Persons.person_id
Ref: Cars.person_id > Persons.person_id
Ref: PhoneNumbers.operator_id > TelecomOperators.operator_id
Ref: PhoneNumbers.region_id > Regions.region_id
Ref: PhoneNumbers.topic_id > Topics.topic_id
Ref: PhonebookNames.phone_id > PhoneNumbers.phone_id
Ref: ImsiNumbers.phone_id > PhoneNumbers.phone_id
Ref: Emails.person_id > Persons.person_id
Ref: Emails.topic_id > Topics.topic_id
Ref: Credentials.person_id > Persons.person_id
Ref: InternetAccounts.service_id > InternetServices.service_id
Ref: InternetAccounts.city_id > Cities.city_id
Ref: InternetAccounts.profile_image_id > Images.image_id
Ref: InternetAccounts.screenshot_id > Images.image_id
Ref: InternetAccounts.person_id > Persons.person_id
Ref: InternetAccounts.topic_id > Topics.topic_id
Ref: WebPages.screenshot_id > Images.image_id
Ref: WebPages.person_id > Persons.person_id
Ref: OnlineCommunities.profile_image_id > Images.image_id
Ref: OnlineCommunities.screenshot_id > Images.image_id
Ref: OnlineCommunities.service_id > InternetServices.service_id
Ref: OnlineCommunities.theme_id > CommunityThemes.theme_id

// Связи для связующих таблиц
Ref: IncomingOutgoing.incoming_id > Incoming.incoming_id
Ref: IncomingOutgoing.outgoing_id > Outgoing.outgoing_id
Ref: IncomingTasks.incoming_id > Incoming.incoming_id
Ref: IncomingTasks.task_id > Tasks.task_id
Ref: OutgoingTasks.outgoing_id > Outgoing.outgoing_id
Ref: OutgoingTasks.task_id > Tasks.task_id
Ref: TaskRelations.task1_id > Tasks.task_id
Ref: TaskRelations.task2_id > Tasks.task_id
Ref: TaskRelations.relation_type_id > TaskRelationTypes.relation_type_id
Ref: TaskPersons.task_id > Tasks.task_id
Ref: TaskPersons.person_id > Persons.person_id
Ref: TaskPhoneNumbers.task_id > Tasks.task_id
Ref: TaskPhoneNumbers.phone_id > PhoneNumbers.phone_id
Ref: TaskInternetAccounts.task_id > Tasks.task_id
Ref: TaskInternetAccounts.internet_accounts_id > InternetAccounts.internet_accounts_id
Ref: TaskEmails.task_id > Tasks.task_id
Ref: TaskEmails.email_id > Emails.email_id
Ref: PersonPhoneNumbers.person_id > Persons.person_id
Ref: PersonPhoneNumbers.phone_id > PhoneNumbers.phone_id
Ref: ImeiImsi.imei_id > ImeiNumbers.imei_id
Ref: ImeiImsi.imsi_id > ImsiNumbers.imsi_id
Ref: CommunityMembers.online_communities_id > OnlineCommunities.online_communities_id
Ref: CommunityMembers.internet_accounts_id > InternetAccounts.internet_accounts_id
Ref: PersonLocations.person_id > Persons.person_id
Ref: PersonLocations.location_id > Locations.location_id
Ref: PersonLocations.address_type_id > AddressTypes.address_type_id
Ref: PersonRelations.person1_id > Persons.person_id
Ref: PersonRelations.person2_id > Persons.person_id
Ref: PersonRelations.relation_type_id > PersonRelationTypes.relation_type_id
Ref: AccountRelations.account1_id > InternetAccounts.internet_accounts_id
Ref: AccountRelations.account2_id > InternetAccounts.internet_accounts_id
Ref: AccountRelations.relation_type_id > AccountRelationTypes.relation_type_id