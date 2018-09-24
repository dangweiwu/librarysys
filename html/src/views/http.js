import axios from 'axios'

var http = axios.create({
    xsrfCookieName:'csrftoken',
    xsrfHeaderName:'X-CSRFToken',
    // withCredentials: true
})


export default http