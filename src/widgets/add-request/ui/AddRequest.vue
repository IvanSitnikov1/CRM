<template>
  <PopUp @onClose="closeAddRequest"
         @onOpen="openAddRequest"
         :data="{
            title: 'Add Request?',
            open: state.showAddRequest
          }">
    <template #content>
        <Tabs :data="{
            tabs: tabs,
            activeTab: store.activeTab
          }" @onTab="handlerChangeTab">
          <template #Days>
            Дни
          </template>
          <template #Hours>
            Часы
          </template>
        </Tabs>
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
import { Calendar } from '@/widgets/calendar'
import { Tabs } from '@/shared/ui/tabs'

const modalStore = useModalStore();

const { state } = storeToRefs(modalStore);

const store = reactive({
  activeTab: 0
})

const tabs = [
  { label: 'Days' },
  { label: 'Hours' }
]

const handlerChangeTab = (value: number) => {
  store.activeTab = value;
}

const closeAddRequest = () => {
  state.value.showAddRequest = false
  unlock()
};

const openAddRequest = () => {
  lock()
};
</script>


<style lang="scss">
  @import "style.module";


</style>
