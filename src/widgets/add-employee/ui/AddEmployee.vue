<template>
  <PopUp @onClose="closeAddEmployee"
         @onOpen="openAddEmployee"
         :data="{
            title: 'Add Employee?',
            open: state.showAddEmployee
          }">
    <template #content>
      <form class="support">
        <UISelect :data="{
          text: 'Member’s Email',
          isMultipleSelect: true
        }"/>
        <UiButton :data="{
          title: 'Approve',
          type: 'submit'
        }"/>
      </form>
    </template>
  </PopUp>
</template>

<script setup lang="ts">
import { PopUp } from '@/entities/popup'
import { UiButton } from '@/shared/ui/button'
import { UISelect } from "@/shared/ui/select";
import { lock, unlock } from "@/shared/lib/ustils/isBlockScroll";
import { useModalStore } from '@/entities/add-modal'
import { storeToRefs } from 'pinia'

const modalStore = useModalStore();

const { state } = storeToRefs(modalStore);
const closeAddEmployee = () => {
  state.value.showAddEmployee = false
  unlock()
};
const openAddEmployee = () => {
  lock()
};
</script>


<style lang="scss">
  @import "style.module";


</style>
