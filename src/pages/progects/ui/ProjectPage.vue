<template>
  <section class="projects-page">
    <PopUp :data="{
        open: false,
        title: 'time',
      }">
      <template #content>
      </template>
    </PopUp>
    <Header class="wrapper wrapper_title" :data="{
      title: 'Projects'
    }"/>
    <main class="wrapper">
      <CardProjectSmall class="projects-page__current-project" :data="{
        id: 'PN0001245',
        title: 'Medical App (iOS native)',
      }"/>
      <div class="projects-page__filter">
        <Title :data="{
          title: 'Tasks',
          isHighLeading: true
        }"/>
        <div class="projects-page__filter-icon">
          <IconBase :data="{
            iconName: 'search'
          }"/>
        </div>
      </div>
      <Collapse @onExpanded="handlerShowTask" :data="{
        isExpanded: state.activeTasks.show
      }">
        <template #header>
          <div class="projects-page__group">
            <Title class="projects-page__group-name" :data="{
              title: 'Active Tasks',
              size: 'small',
              isHighLeading: true
            }"/>
          </div>
        </template>
        <template #content>
          <Collapse @onExpanded="handlerShowTaskDev" :data="{
            isExpanded: state.activeTasks.showDevelopment,
            title: 'Development (5 issues)'
          }">
            <template #content>
              <div class="projects-page__tasks">
                <CardTask data="" v-for="index in 5" :key="index"/>
              </div>
            </template>
          </Collapse>
          <Collapse @onExpanded="handlerShowTaskDes" :data="{
            isExpanded: state.activeTasks.showDesign,
            title: 'Design (2 issues)'
          }">
            <template #content>
              <div class="projects-page__tasks">
                <CardTask data="" v-for="index in 2" :key="index"/>
              </div>
            </template>
          </Collapse>
        </template>
      </Collapse>
    </main>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { TimePicker } from '@/shared/ui/time-picker'
import { PopUp } from '@/entities/popup'
import { Header } from '@/shared/ui/header'
import { CardProjectSmall } from "@/entities/project-small";
import { Title } from "@/shared/ui/title";
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";
import { Collapse } from "@/shared/ui/collaps";
import { CardTask } from "@/entities/task";

useHead({
  title: 'Projects'
})

const state = reactive({
  activeTasks: {
    show: true,
    showDesign: true,
    showDevelopment: true,
    showTesting: true,
    showMarketing: true,
    showProjectManagement: true,
  }
})

const handlerShowTask = (value: boolean) => {
  state.activeTasks.show = value;
}

const handlerShowTaskDev = (value: boolean) => {
  state.activeTasks.showDevelopment = value;
}

const handlerShowTaskDes = (value: boolean) => {
  state.activeTasks.showDesign = value;
}


/*onBeforeUnmount(() => {
  bookModel.$reset()
})*/
</script>

<style lang="scss">
.projects-page {
  &__current-project {
    margin-bottom: 32px;
  }
  &__filter {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }
  &__filter-icon {
    align-self: center;
    width: 48px;
    height: 48px;
    border-radius: 14px;
    box-shadow: 0 6px 58px 0 rgba(196, 203, 214, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
  }
  &__group {
    border-radius: 14px;
    background: rgb(230, 237, 245);
    padding: 12px 0;
    margin-bottom: 20px;
  }
  &__tasks {
    display: flex;
    flex-direction: column;
    row-gap: 20px;
  }
  &__group-name {
    max-width: max-content;
    margin: 0 auto;
  }
}
</style>
