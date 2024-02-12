import axios from 'axios'

export const http = axios.create({
  baseURL: import.meta.env.VITE_BASE_URL,
  headers: {
    'Content-type': 'application/json',
    'Authorization': localStorage.getItem('token')
  }
})

http.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    if (error.response && error.response.status === 401) {
      try {
        const refreshToken = localStorage.getItem('refreshToken');
        console.log(refreshToken);
        const request = await axios.post('http://localhost:3000/auth/refresh', {
          refreshToken,
          agent: navigator.userAgent,
        })
        console.log(request);
      } catch (refreshError) {
        throw refreshError;
      }
    }

    throw error;
  }
);
