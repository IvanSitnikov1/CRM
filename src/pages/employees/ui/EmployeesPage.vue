<template>
  <section class="employees-page">
    <Header class="wrapper wrapper_title" :data="{
      title: 'Employees'
    }"/>
    <div class="wrapper">
      <Tabs>
        <template #List>
          <RecycleScroller
            class="employees-page__employees"
            :items="list"
            :item-size="290"
            key-field="id"
            v-slot="{ item }"
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
          <p>This is the content for Tab 1.</p>
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
import { useScrollLock } from '@vueuse/core'
import { Tabs } from '@/shared/ui/tabs'

useHead({
  title: 'Employees'
})

const isLocked = useScrollLock(document.body)

isLocked.value = true;

const generateHours = () => new Array(70).fill(1).map((v, i) => {
  return { id: i + 1, text: i + 1}
})

const list = generateHours();

/*onBeforeUnmount(() => {
  bookModel.$reset()
})*/
</script>

<style lang="scss">
.employees-page {
  &__employees {
    height: calc(100vh - 270px);
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
  }
  &__position {
    display: flex;
    column-gap: 12px;
    align-items: center;
  }
  &__description {
    color: rgb(10, 22, 41);
    font-size: 16px;
    line-height: 150%;
  }
}
</style>
