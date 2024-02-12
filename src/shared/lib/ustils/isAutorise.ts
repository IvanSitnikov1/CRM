import { useLocalStorage } from '@vueuse/core';

const accessToken = useLocalStorage<string>('token', null);
export const isAuthenticated = computed(() => !!accessToken.value);

