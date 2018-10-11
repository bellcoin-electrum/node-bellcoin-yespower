var use_yespower = 1;

if(!use_yespower) {
    module.exports = require('bindings')('bitzeny_yescrypt');
} else {
    module.exports = require('bindings')('bitzeny_yespower');
}
