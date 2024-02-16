<template>
  <PopUp @onClose="closeSupport" :data="{
    title: 'Add Employee?',
    open: app.showAddEmployee
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
import { useAppModel } from '@/entities/app'
import { PopUp } from '@/entities/popup'
import { UiButton } from '@/shared/ui/button'
import { UISelect } from "@/shared/ui/select";
import { lock, unlock } from "@/shared/lib/ustils/isBlockScroll";

const app = useAppModel()


const closeSupport = () => {
  app.updateShowAddEmployee(false)
};

watch(() => app.showAddEmployee, (value) => {
  if (value) {
    lock()
  } else {
    unlock()
  }
})
</script>


<style lang="scss">
  @import "style.module";


</style>
