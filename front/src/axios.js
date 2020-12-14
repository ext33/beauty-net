import axios from "axios";

const url = 'http://localhost:8000/api/v2/'
const request = axios.create({
    baseURL: url
})


let api = {
   async get_signup(id) {
       let result
       let status_code = 200
       let response = await request.get(url + 'signup-by-pk/' + id).catch(error => {
           if (error.response.status === 404){
               status_code = 404
           }
           else {
               status_code = 500
           }
       })
       if (status_code === 200){
           result = response.data
       }
       else if (status_code === 404){
           result = 404
       }
       else {
           result = 500
       }
       return result
   },

}


export default api