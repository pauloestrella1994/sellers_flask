CREATE TABLE `sellers` (
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `id` varchar(36) NOT NULL,
  `brand` varchar(256) NOT NULL,
  `mobile_phone` varchar(16) NOT NULL,
  `about` text DEFAULT NULL,
  `cnpj` varchar(14) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `iugu_account_id` varchar(64) NOT NULL,
  `origin` varchar(16) NOT NULL,
  `blocked` tinyint(1) NOT NULL,
  `paused` tinyint(1) NOT NULL,
  `certificate_url` varchar(200) NOT NULL,
  `ctr` varchar(14) NOT NULL,
  `features` varchar(256) NOT NULL,
  `ie` varchar(14) NOT NULL,
  `status` varchar(14) NOT NULL,
  `terms_of_use_version` decimal(10,0) NOT NULL,
  `logo_url` varchar(200) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `account_executive_id` varchar(36) DEFAULT NULL,
  `invite_id` varchar(36) DEFAULT NULL,
  `invoice_default_serial_number` decimal(10,0) NOT NULL,
  `business_type` varchar(255) NOT NULL,
  `invoice_initial_number` decimal(10,0) NOT NULL,
  `owner_id` varchar(36) DEFAULT NULL,
  `branded_stores` varchar(256) NOT NULL,
  `last_blocked_on` varchar(256) NOT NULL,
  `blocked_reason` varchar(64) NOT NULL,
  `has_withdraw_rejection` tinyint(1) NOT NULL,
  `olist_responsible` varchar(254) NOT NULL,
  `signup_origin` varchar(32) DEFAULT NULL,
  `plan_type` varchar(16) DEFAULT NULL,
  `search_vector` text DEFAULT NULL,
  `portifolio_size` decimal(10,0) NOT NULL,
  `is_manufacturer` tinyint(1) NOT NULL,
  `payment_blocked` tinyint(1) DEFAULT NULL,
  `payment_blocked_reason` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1