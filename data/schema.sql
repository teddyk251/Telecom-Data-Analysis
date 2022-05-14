CREATE TABLE IF NOT EXISTS `user_satisfaction` (`user_id` VARCHAR(255) NOT NULL,
`satisfaction_score` FLOAT NOT NULL,
`engagement_score` FLOAT NOT NULL,
`experience_score` FLOAT NOT NULL,
PRIMARY KEY(`user_id`)
) ENGINE = InnoDB  DEFAULT CHARSET = utf8mb4 COLLATE utf8mb4_unicode_ci ;