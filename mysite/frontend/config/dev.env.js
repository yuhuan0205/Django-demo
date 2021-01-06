'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  APIPATH: '"http://192.168.111.166:8070"',//192.168.111.43
  DORENTO: '`client/api?mode=${mode}&date1=${date1}&date2=${date2}&clientname=${cli}&productname=${pro}&campaign=${cam}&ordertype=${ord}&regular=${reg}&paymethod=${pay}&media=${media}&link_type=${link}&ga1=${ga1}&ga2=${ga2}&ga3=${ga3}`',
  DORENTO_FILTER: '`client/api?mode=${mode}&date1=${date1}&date2=${date2}&clientname=${cli}&productname=${pro}&campaign=${cam}&ordertype=${ord}&regular=${reg}&paymethod=${pay}&media=${media}&link_type=${link}&ga1=${ga1}&ga2=${ga2}&ga3=${ga3}`',
  DORENTO_DOWNLOAD: '`client/download?mode=${mode}&date1=${date1}&date2=${date2}&clientname=${cli}&productname=${pro}&campaign=${cam}&ordertype=${ord}&regular=${reg}&paymethod=${pay}&media=${media}&link_type=${link}&ga1=${ga1}&ga2=${ga2}&ga3=${ga3}`',

})
