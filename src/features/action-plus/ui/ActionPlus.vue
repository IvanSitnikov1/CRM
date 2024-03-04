<template>
    <article
        class="actions"
        @click="handlerOpenAddModal($route)"
    >
        <span class="actions__plus">+</span>
    </article>
</template>

<script setup lang="ts">
import { type IModalType, useModalStore } from '@/entities/add-modal'

const modalStore = useModalStore();

type ConfigItem = {
  route: string;
  type: IModalType
}
const config: ConfigItem[] = [
  { route: 'home', type: 'all' },
  { route: 'nears-events', type: 'event' },
  { route: 'calendar', type: 'event' },
  { route: 'projects', type: 'task' },
  { route: 'vacations', type: 'request' },
  { route: 'employees', type: 'employee' },
  { route: 'profile', type: 'all' },
  { route: 'my-profile', type: 'all' },
]

const { openModalAdd } = modalStore;

const handlerOpenAddModal = path => {
  const currentRoute = path.name;
  const modalType = config.find(item => item.route === currentRoute).type;
  openModalAdd(modalType)
};
</script>

<style lang="scss">
  @import "style.module";
</style>
