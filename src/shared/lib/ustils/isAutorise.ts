import { ref, onMounted } from 'vue';

export const isAuthenticated = ref(localStorage.getItem('token') !== null);
