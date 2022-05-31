var mysql = require('mysql2');
require('dotenv').config();

class DatabaseUsers {
    constructor(config) {
        this.connection = mysql.createPool({
            host: process.env.MYSQL_HOST,
            user: process.env.MYSQL_USER,
            password: process.env.MYSQL_PASSWORD,
            database: process.env.MYSQL_DATABASE_USER,
            connectionLimit: 10
        });
    }
    query(sql, args) {
        return new Promise((resolve, reject) => {
            this.connection.query(sql, args, (err, rows) => {
                if (err) return reject(err);
                resolve(rows);
            });
        });
    }
    close() {
        return new Promise((resolve, reject) => {
            this.connection.end(err => {
                if (err) return reject(err);
                resolve();
            });
        });
    }
}

module.exports = new DatabaseUsers();