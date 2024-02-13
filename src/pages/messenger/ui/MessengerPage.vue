<template>
  <section class="projects-page">
    <Header class="wrapper wrapper_title" :data="{
      title: 'Messenger'
    }"/>
    <div class="wrapper_big">
      <div class="projects-page__content">
        <div class="projects-page__header">
          <Title :data="{
            isHighLeading: true,
            size: 'medium',
            title: 'Conversations',
          }"/>
          <div class="projects-page__icons">
            <img src="@/shared/assets/icons/search.svg" alt="search">
            <img src="@/shared/assets/icons/search.svg" alt="add">
          </div>
        </div>
        <hr class="projects-page__line">
        <div class="projects-page__groups">
          <Collapse @onExpanded="handlerExpandedGroups"
                    :data="{
                      title: 'Groups',
                      isExpanded: state.groups
                    }">
            <template #content>
              <div class="projects-page__messages">
                <CardMessage :data="{}"
                             v-for="index in 2"
                             :key="index"/>
              </div>
            </template>
          </Collapse>
          <Collapse @onExpanded="handlerExpandedDirectMessages"
                    :data="{
                      title: 'Direct Messages',
                      isExpanded: state.directMessages
                    }">
            <template #content>
              <div class="projects-page__messages">
                <CardMessage :data="{}"
                             v-for="index in 6"
                             :key="index"/>
              </div>
            </template>
          </Collapse>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { Collapse } from '@/shared/ui/collaps'
import { Header } from '@/shared/ui/header'
import { Title } from '@/shared/ui/title'
import { CardMessage } from "@/entities/message";

const state = reactive({
  groups: true,
  directMessages: true,
})


const handlerExpandedGroups = (value: boolean) => {
  state.groups = value
}

const handlerExpandedDirectMessages = (value: boolean) => {
  state.directMessages = value
}

</script>

<style lang="scss">
.projects-page {
  &__groups {
    display: flex;
    flex-direction: column;
    row-gap: 16px;
    padding: 0 20px 16px;
  }
  &__header {
    padding: 24px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  &__icons {
    display: flex;
    column-gap: 24px;
  }
  &__content {
    border-radius: 24px;
    box-shadow: 0 6px 58px 0 rgba(196, 203, 214, 0.1);
    background-color: rgb(255, 255, 255);
    margin-bottom: 52px;
  }
  &__messages {
    display: flex;
    margin-top: 8px;
    flex-direction: column;
    row-gap: 8px;
  }
  &__line {
    margin-top: 0;
    margin-bottom: 20px;
  }
}
</style>
