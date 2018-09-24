import axios from 'axios'

var http = axios.create({
    // baseURL:'http://127.0.0.1:8000',
    xsrfCookieName:'csrftoken',
    xsrfHeaderName:'X-CSRFToken',
    // withCredentials: true
})

http.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    return response;
  }, function (error) {
    if(error.response.status==401){
        localStorage.setItem('token',null)
    }
    return Promise.reject(error);
  });

export default http