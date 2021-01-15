"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _axios = _interopRequireDefault(require("axios"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(source, true).forEach(function (key) { _defineProperty(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(source).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

// const url = 'http://localhost:8000/api/' //for dev
var url = 'http://localhost:8080/api/'; // for prod

var request = _axios["default"].create({
  baseURL: url
});

var api = {
  check_only_error: function check_only_error(data, router) {
    var result;
    return regeneratorRuntime.async(function check_only_error$(_context) {
      while (1) {
        switch (_context.prev = _context.next) {
          case 0:
            if (!(data === 404)) {
              _context.next = 5;
              break;
            }

            _context.next = 3;
            return regeneratorRuntime.awrap(router.push({
              path: '/error'
            }));

          case 3:
            _context.next = 11;
            break;

          case 5:
            if (!(data === 500)) {
              _context.next = 10;
              break;
            }

            _context.next = 8;
            return regeneratorRuntime.awrap(router.push({
              path: '/error'
            }));

          case 8:
            _context.next = 11;
            break;

          case 10:
            result = data;

          case 11:
            return _context.abrupt("return", result);

          case 12:
          case "end":
            return _context.stop();
        }
      }
    });
  },
  check_error_404: function check_error_404(data, router) {
    var result;
    return regeneratorRuntime.async(function check_error_404$(_context2) {
      while (1) {
        switch (_context2.prev = _context2.next) {
          case 0:
            if (!(data === 404)) {
              _context2.next = 5;
              break;
            }

            _context2.next = 3;
            return regeneratorRuntime.awrap(router.push({
              path: '/error'
            }));

          case 3:
            _context2.next = 11;
            break;

          case 5:
            if (!(data === 500)) {
              _context2.next = 10;
              break;
            }

            _context2.next = 8;
            return regeneratorRuntime.awrap(router.push({
              path: '/error'
            }));

          case 8:
            _context2.next = 11;
            break;

          case 10:
            result = data;

          case 11:
            return _context2.abrupt("return", result);

          case 12:
          case "end":
            return _context2.stop();
        }
      }
    });
  },
  get_signup: function get_signup(id) {
    var result, status_code, response;
    return regeneratorRuntime.async(function get_signup$(_context3) {
      while (1) {
        switch (_context3.prev = _context3.next) {
          case 0:
            status_code = 200;
            _context3.next = 3;
            return regeneratorRuntime.awrap(request.get(url + 'signup-by-pk/' + id)["catch"](function (error) {
              if (error.response.status === 404) {
                status_code = 404;
              } else {
                status_code = 500;
              }
            }));

          case 3:
            response = _context3.sent;

            if (status_code === 200) {
              result = response.data;
            } else if (status_code === 404) {
              result = 404;
            } else {
              result = 500;
            }

            return _context3.abrupt("return", result);

          case 6:
          case "end":
            return _context3.stop();
        }
      }
    });
  },
  services_master: function services_master(master_id) {
    var result, status_code, response;
    return regeneratorRuntime.async(function services_master$(_context4) {
      while (1) {
        switch (_context4.prev = _context4.next) {
          case 0:
            status_code = 200;
            _context4.next = 3;
            return regeneratorRuntime.awrap(request.get(url + 'services-list/' + master_id)["catch"](function (error) {
              if (error.response.status === 404) {
                status_code = 404;
              } else {
                status_code = 500;
              }
            }));

          case 3:
            response = _context4.sent;

            if (status_code === 200) {
              result = response.data;
            } else if (status_code === 404) {
              result = 404;
            } else {
              result = 500;
            }

            return _context4.abrupt("return", result);

          case 6:
          case "end":
            return _context4.stop();
        }
      }
    });
  },
  list_services: function list_services() {
    var result, status_code, response;
    return regeneratorRuntime.async(function list_services$(_context5) {
      while (1) {
        switch (_context5.prev = _context5.next) {
          case 0:
            status_code = 200;
            _context5.next = 3;
            return regeneratorRuntime.awrap(request.get(url + 'services-list/')["catch"](function (error) {
              if (error.response.status === 404) {
                status_code = 404;
              } else {
                status_code = 500;
              }
            }));

          case 3:
            response = _context5.sent;

            if (status_code === 200) {
              result = response.data;
            } else if (status_code === 404) {
              result = 404;
            } else {
              result = 500;
            }

            return _context5.abrupt("return", result);

          case 6:
          case "end":
            return _context5.stop();
        }
      }
    });
  },
  list_personal: function list_personal(office_id) {
    var result, status_code, response;
    return regeneratorRuntime.async(function list_personal$(_context6) {
      while (1) {
        switch (_context6.prev = _context6.next) {
          case 0:
            status_code = 200;
            _context6.next = 3;
            return regeneratorRuntime.awrap(request.get(url + 'personal-list/' + office_id)["catch"](function (error) {
              if (error.response.status === 404) {
                status_code = 404;
              } else {
                status_code = 500;
              }
            }));

          case 3:
            response = _context6.sent;

            if (status_code === 200) {
              result = response.data;
            } else if (status_code === 404) {
              result = 404;
            } else {
              result = 500;
            }

            return _context6.abrupt("return", result);

          case 6:
          case "end":
            return _context6.stop();
        }
      }
    });
  },
  list_offices: function list_offices() {
    var result, status_code, response;
    return regeneratorRuntime.async(function list_offices$(_context7) {
      while (1) {
        switch (_context7.prev = _context7.next) {
          case 0:
            status_code = 200;
            _context7.next = 3;
            return regeneratorRuntime.awrap(request.get(url + 'offices-list')["catch"](function (error) {
              if (error.response.status === 404) {
                status_code = 404;
              } else {
                status_code = 500;
              }
            }));

          case 3:
            response = _context7.sent;

            if (status_code === 200) {
              result = response.data;
            } else if (status_code === 404) {
              result = 404;
            } else {
              result = 500;
            }

            return _context7.abrupt("return", result);

          case 6:
          case "end":
            return _context7.stop();
        }
      }
    });
  },
  list_times: function list_times(master_id) {
    var result, status_code, response;
    return regeneratorRuntime.async(function list_times$(_context8) {
      while (1) {
        switch (_context8.prev = _context8.next) {
          case 0:
            status_code = 200;
            _context8.next = 3;
            return regeneratorRuntime.awrap(request.get(url + 'signup-time/' + master_id)["catch"](function (error) {
              if (error.response.status === 404) {
                status_code = 404;
              } else {
                status_code = 500;
              }
            }));

          case 3:
            response = _context8.sent;

            if (status_code === 200) {
              result = response.data;
            } else if (status_code === 404) {
              result = 404;
            } else {
              result = 500;
            }

            return _context8.abrupt("return", result);

          case 6:
          case "end":
            return _context8.stop();
        }
      }
    });
  },
  cancel_signup: function cancel_signup(id) {
    var result, status_code, response;
    return regeneratorRuntime.async(function cancel_signup$(_context9) {
      while (1) {
        switch (_context9.prev = _context9.next) {
          case 0:
            status_code = 200;
            _context9.next = 3;
            return regeneratorRuntime.awrap(request.get(url + 'signup-cancel/' + id)["catch"](function (error) {
              if (error.response.status === 404) {
                status_code = 404;
              } else {
                status_code = 500;
              }
            }));

          case 3:
            response = _context9.sent;

            if (status_code === 200) {
              result = response.data;
            } else if (status_code === 404) {
              result = 404;
            } else {
              result = 500;
            }

            return _context9.abrupt("return", result);

          case 6:
          case "end":
            return _context9.stop();
        }
      }
    });
  },
  set_signup: function set_signup(name, service, master, datetime, office) {
    var result, status_code, FormData, data, response;
    return regeneratorRuntime.async(function set_signup$(_context10) {
      while (1) {
        switch (_context10.prev = _context10.next) {
          case 0:
            status_code = 200;
            FormData = require('form-data');
            data = new FormData();
            data.append('FIO', name);
            data.append('service', service);
            data.append('time', datetime);
            data.append('master', master);
            data.append('branch_office', office);
            _context10.next = 10;
            return regeneratorRuntime.awrap(request.post(url + 'create-signup/', data, {
              headers: _objectSpread({}, data.getHeaders)
            })["catch"](function (error) {
              if (error.response.status === 404) {
                status_code = 404;
              } else {
                status_code = 500;
              }
            }));

          case 10:
            response = _context10.sent;

            if (status_code === 200) {
              result = response.data;
            } else if (status_code === 404) {
              result = 404;
            } else {
              result = 500;
            }

            return _context10.abrupt("return", result);

          case 13:
          case "end":
            return _context10.stop();
        }
      }
    });
  }
};
var _default = api;
exports["default"] = _default;