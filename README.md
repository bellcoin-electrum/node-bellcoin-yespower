BitZeny yescrypt for Node.js
============================

## Prerequisites
* Node.js

## Build
```
git clone https://github.com/BitzenyCoreDevelopers/node-bitzeny-yescrypt.git && cd node-bitzeny-yescrypt
npm install
```

## Example Code
```javascript
var bitzeny_yescrypt = require('bitzeny-yescrypt');

var data = new Buffer("7000000001e980924e4e1109230383e66d62945ff8e749903bea4336755c00000000000051928aff1b4d72416173a8c3948159a09a73ac3bb556aa6bfbcad1a85da7f4c1d13350531e24031b939b9e2b", "hex");
console.log(bitzeny_yescrypt.hash(data).toString('hex'));
```
