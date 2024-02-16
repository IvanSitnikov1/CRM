import { useScrollLock } from '@vueuse/core';

const app = ref<HTMLElement | null>(document.body);
const isLocked = useScrollLock(app);

export const unlock = () => {
  isLocked.value = false;
};
export const lock = () => {
  isLocked.value = true;
};
