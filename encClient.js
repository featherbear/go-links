const crypto = require('crypto')

module.exports = function generate(message, password) {
    const SALT = crypto.randomBytes(16) 
    const key = crypto.pbkdf2Sync(password, SALT, 100000, 32, 'sha256')
    
    const cipher = crypto.createCipheriv('aes-256-cbc', key, SALT)
    const aes = cipher.update(message, 'utf-8')
    const aes_final = cipher.final()

    return Buffer.concat([SALT, aes, aes_final]).toString('base64')
}