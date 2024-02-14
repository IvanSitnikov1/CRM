<template>
  <section class="employees-page">
    <Header class="wrapper wrapper_title" :data="{
      title: 'Employees'
    }"/>
    <div class="wrapper">
      <Tabs :data="{
        tabs: tabs,
        activeTab: store.activeTab
      }" @onTab="handlerChangeTab">
        <template #List>
          <RecycleScroller
            class="employees-page__employees"
            :items="list"
            :item-size="288"
            :page-mode="true"
            key-field="id"
          >
            <CardEmployee
              :data="{
                job: 'zu@pasajpot.org',
                name: 'Samuel Curry',
                isShowLine: true,
                isBorderRound: true,
                isShadow: true,
              }"
            >
              <template #content>
                <div class="employees-page__info">
                  <div class="employees-page__column">
                    <div class="employees-page__title">Gender</div>
                    <div class="employees-page__date">{{ new Date().getFullYear()}}</div>
                  </div>
                  <div class="employees-page__column">
                    <div class="employees-page__title">Birthday</div>
                    <div class="employees-page__date">{{ new Date().getFullYear()}}</div>
                  </div>
                  <div class="employees-page__column">
                    <div class="employees-page__title">Full age</div>
                    <div class="employees-page__date">{{ new Date().getDate()}}</div>
                  </div>
                </div>
                <div class="employees-page__job">
                  <div class="employees-page__title">
                    Position
                  </div>
                  <div class="employees-page__position">
                  <span class="employees-page__description">
                    UI/UX Designer
                  </span>
                    <Tag :data="{
                    text: 'Middle'
                  }"/>
                  </div>
                </div>
              </template>
            </CardEmployee>
          </RecycleScroller>
        </template>
        <template #Activity>
          <RecycleScroller
            class="employees-page__employees"
            :items="list"
            :item-size="336"
            :page-mode="true"
            key-field="id"
          >
            <Card
              :data="{
                    isWhite: false,
                    isBox: true,
                    fullName: 'Shawn Stone',
                    tag: 'Middle',
                    job: 'UI/UX Designer',
                    image: 'https://cdn.tripster.ru/thumbs2/f5a8c1fe-b128-11ed-9e63-2e5ef03bee8d.1220x600.jpeg',
                  }"
              >
              <template #content>
                <div class="employees-page__task">
                  <div class="employees-page__column employees-page__column_center">
                    <div class="employees-page__date employees-page__date_big">0</div>
                    <div class="employees-page__about">Backlog
                      tasks</div>
                  </div>
                  <div class="employees-page__column employees-page__column_center">
                    <div class="employees-page__date employees-page__date_big">16</div>
                    <div class="employees-page__about">Tasks
                      In Progress</div>
                  </div>
                  <div class="employees-page__column employees-page__column_center">
                    <div class="employees-page__date employees-page__date_big">6</div>
                    <div class="employees-page__about">Tasks
                      In Review</div>
                  </div>
                </div>
              </template>
            </Card>
          </RecycleScroller>
        </template>
      </Tabs>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { Header } from '@/shared/ui/header'
import { CardEmployee } from '@/entities/employee'
import { Tag } from '@/shared/ui/tag'
import { Tabs } from '@/shared/ui/tabs'
import { Card } from '@/entities/user'

useHead({
  title: 'Employees'
})

const generateHours = () => new Array(700).fill(1).map((v, i) => {
  return { id: i + 1, text: i + 1}
})

const list = generateHours();
const tabs = [
  { label: 'List' },
  { label: 'Activity' }
]

const store = reactive({
  activeTab: 0
})

const handlerChangeTab = (value: number) => {
  store.activeTab = value;
}

/*onBeforeUnmount(() => {
  bookModel.$reset()
})*/
</script>

<style lang="scss">
.employees-page {
  &__employees {
    height: 100%;
    margin-bottom: 52px;
  }
  &__info {
    display: flex;
    margin: 24px 0;
    justify-content: space-between;
  }
  &__title {
    margin-bottom: 4px;
  }
  &__date {
    font-size: 16px;
    color: rgb(10, 22, 41);
    line-height: 150%;
    &_big {
      font-size: 26px;
      font-weight: 700;
      margin-bottom: 12px;
    }
  }
  &__position {
    display: flex;
    column-gap: 12px;
    align-items: center;
  }
  &__column {
    &_center {
      text-align: center;
    }
  }
  &__description {
    color: rgb(10, 22, 41);
    font-size: 16px;
    line-height: 150%;
  }
  &__task {
    margin-top: 24px;
    display: flex;
    justify-content: space-around;
  }
}
</style>
