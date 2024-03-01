<template>
    <section class="projects-page">
        <HeaderPage />
        <main class="wrapper">
            <CardProjectSmall
                class="projects-page__current-project"
                :data="{
                    id: 'PN0001245',
                    title: 'Medical App (iOS native)',
                }"
            />
            <div class="projects-page__filter">
                <Title
                    :data="{
                        title: 'Tasks',
                        isHighLeading: true,
                    }"
                />
                <div class="projects-page__filter-icon">
                    <IconBase
                        :data="{
                            iconName: 'search',
                        }"
                    />
                </div>
            </div>
            <div class="projects-page__groups">
                <Collapse
                    @onExpanded="handlerShowTask"
                    :data="{
                        isExpanded: state.activeTasks.show,
                    }"
                >
                    <template #header>
                        <div
                            class="projects-page__group"
                            :class="{ 'projects-page__group_active': !state.activeTasks.show }"
                        >
                            <Title
                                class="projects-page__group-name"
                                :class="{ 'projects-page__group-name_active': !state.activeTasks.show }"
                                :data="{
                                    title: 'Active Tasks',
                                    size: 'small',
                                    isHighLeading: true,
                                }"
                            />
                        </div>
                    </template>
                    <template #content>
                        <div class="projects-page__inner-groups">
                            <Collapse
                                @onExpanded="handlerShowTaskDev"
                                :data="{
                                    isExpanded: state.activeTasks.showDevelopment,
                                    title: 'Development (5 issues)',
                                }"
                            >
                                <template #content>
                                    <div class="projects-page__tasks">
                                        <CardTask
                                            data=""
                                            v-for="index in 5"
                                            :key="index"
                                        />
                                    </div>
                                </template>
                            </Collapse>
                            <Collapse
                                @onExpanded="handlerShowTaskDes"
                                :data="{
                                    isExpanded: state.activeTasks.showDesign,
                                    title: 'Design (2 issues)',
                                }"
                            >
                                <template #content>
                                    <div class="projects-page__tasks">
                                        <CardTask
                                            data=""
                                            v-for="index in 2"
                                            :key="index"
                                        />
                                    </div>
                                </template>
                            </Collapse>
                        </div>
                    </template>
                </Collapse>
                <Collapse
                    @onExpanded="handlerShowTask"
                    :data="{
                        isExpanded: state.activeTasks.show,
                    }"
                >
                    <template #header>
                        <div
                            class="projects-page__group"
                            :class="{ 'projects-page__group_active': !state.activeTasks.show }"
                        >
                            <Title
                                class="projects-page__group-name"
                                :class="{ 'projects-page__group-name_active': !state.activeTasks.show }"
                                :data="{
                                    title: 'Backlog',
                                    size: 'small',
                                    isHighLeading: true,
                                }"
                            />
                        </div>
                    </template>
                    <template #content>
                        <div class="projects-page__inner-groups">
                            <Collapse
                                @onExpanded="handlerShowTaskDev"
                                :data="{
                                    isExpanded: state.activeTasks.showDevelopment,
                                    title: 'Development (5 issues)',
                                }"
                            >
                                <template #content>
                                    <div class="projects-page__tasks">
                                        <CardTask
                                            data=""
                                            v-for="index in 5"
                                            :key="index"
                                        />
                                    </div>
                                </template>
                            </Collapse>
                            <Collapse
                                @onExpanded="handlerShowTaskDes"
                                :data="{
                                    isExpanded: state.activeTasks.showDesign,
                                    title: 'Design (2 issues)',
                                }"
                            >
                                <template #content>
                                    <div class="projects-page__tasks">
                                        <CardTask
                                            data=""
                                            v-for="index in 2"
                                            :key="index"
                                        />
                                    </div>
                                </template>
                            </Collapse>
                        </div>
                    </template>
                </Collapse>
            </div>
        </main>
        <PopUp
          :data="{
                  open: false,
                  title: 'Select project',
              }"
        >
          <template #content />
        </PopUp>
    </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue';
import { PopUp } from '@/entities/popup';
import { Header } from '@/shared/ui/header';
import { CardProjectSmall } from '@/entities/project-small';
import { Title } from '@/shared/ui/title';
import { Collapse } from '@/shared/ui/collaps';
import { CardTask } from '@/entities/task';
import { IconBase } from "@/shared/ui/icon-base";
import { HeaderPage } from '@/entities/header-page'

useHead({
  title: 'Projects'
});

const state = reactive({
  activeTasks: {
    show: true,
    showDesign: true,
    showDevelopment: true,
    showTesting: true,
    showMarketing: true,
    showProjectManagement: true
  }
});

const handlerShowTask = value => {
  state.activeTasks.show = value;
};

const handlerShowTaskDev = value => {
  state.activeTasks.showDevelopment = value;
};

const handlerShowTaskDes = value => {
  state.activeTasks.showDesign = value;
};

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
    align-items: center;
  }
  &__inner-groups {
    display: flex;
    flex-direction: column;
    row-gap: 12px;
    margin-bottom: 32px;
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
    transition: background-color ease .4s;
    &_active {
      background: rgb(63, 140, 255);
    }
  }
  &__tasks {
    display: flex;
    flex-direction: column;
    row-gap: 20px;
  }
  &__group-name {
    max-width: max-content;
    margin: 0 auto;
    &_active {
      color: white;
    }
  }
}
</style>
