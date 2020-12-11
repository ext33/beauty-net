const axios = require('axios');
const url = ''

let api = {
   id_check(id) {
    let result
    axios.post(url + 'id-check/', {
        id: id
    }).then(function (response) {
        result = response
    })
    if (result) {
        return 1
    } else {
        return 0
    }
},

}


export default api