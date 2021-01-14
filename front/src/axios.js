import axios from "axios";

const url = 'http://localhost:8000/api/'
const request = axios.create({
    baseURL: url
})


let api = {
    async check_only_error(data, router) {
        let result
        if (data === 404) {
            await router.push({path: '/error'})
        } else if (data === 500) {
            await router.push({path: '/error'})
        } else {
            result = data
        }
        return result
    },

    async check_error_404(data, router) {
        let result
        if (data === 404) {
            await router.push({path: '/error'})
        } else if (data === 500) {
            await router.push({path: '/error'})
        } else {
            result = data
        }
        return result
    },

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

   async services_master(master_id) {
       let result
       let status_code = 200
       let response = await request.get(url + 'services-list/' + master_id).catch(error => {
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

   async list_services() {
       let result
       let status_code = 200
       let response = await request.get(url + 'services-list/').catch(error => {
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

   async list_personal(office_id) {
       let result
       let status_code = 200
       let response = await request.get(url + 'personal-list/' + office_id).catch(error => {
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

   async list_offices() {
       let result
       let status_code = 200
       let response = await request.get(url + 'offices-list').catch(error => {
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

    async list_times(master_id) {
        let result
        let status_code = 200
        let response = await request.get(url + 'signup-time/' + master_id).catch(error => {
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

    async cancel_signup(id) {
        let result
        let status_code = 200
        let response = await request.get(url + 'signup-cancel/' + id).catch(error => {
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

   async set_signup(name, service, master, datetime, office) {
       let result
       let status_code = 200
       let FormData = require('form-data');
       let data = new FormData();
       data.append('FIO', name);
       data.append('service', service);
       data.append('time', datetime);
       data.append('master', master);
       data.append('branch_office', office);
       let response = await request.post(url + 'create-signup/',data ,{
           headers: {
               ...data.getHeaders
           }
       }).catch(error => {
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
   }
}

export default api
