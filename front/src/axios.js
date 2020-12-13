import axios from "axios";

const url = 'http://localhost:8000/api/v2/'
const request = axios.create({
    baseURL: url
})


let api = {
   get_signup(id) {
       let result
       let code = 200
       request.get(url + 'signup-by-pk/' + id
       ).then(function (response) {
           result = response.data
           console.log(result)
           code = response.status
           if (code === 404){
               return 404
           }
           else if (code === 200){
               console.log(result)
               return result
           }
           else {
               return 500
           }
       })

   },

}


export default api