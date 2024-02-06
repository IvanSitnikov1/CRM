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
          <Collapse>
            <template #content>
              <div class="projects-page__messages">
                <article v-for="i in 2" class="message">
                  <div class="message__icon">
                    <img class="message__image" src="@/shared/assets/test.png" alt="icon">
                  </div>
                  <div class="message__info">
                    <Title :data="{
                    title: 'Medical App Team',
                    size: 'small',
                    isHighLeading: true
                  }"/>
                    <div class="message__last">
                      Caroline: Hi guys! I’ve share…
                    </div>
                  </div>
                  <div class="message__data">
                    <time class="message__time">12.04</time>
                    <div class="message__not-read">
                    <span class="message__text-count">
                      12
                    </span>
                    </div>
                  </div>
                </article>
              </div>
            </template>
          </Collapse>
          <Collapse>
            <template #content>
              <div class="projects-page__messages">
                <article v-for="i in 6" class="message">
                  <div class="message__icon">
                    <img class="message__image" src="@/shared/assets/test.png" alt="icon">
                  </div>
                  <div class="message__info">
                    <Title :data="{
                    title: 'Medical App Team',
                    size: 'small',
                    isHighLeading: true
                  }"/>
                    <div class="message__last">
                      Caroline: Hi guys! I’ve share…
                    </div>
                  </div>
                  <div class="message__data">
                    <time class="message__time">12.04</time>
                    <div class="message__not-read">
                    <span class="message__text-count">
                      12
                    </span>
                    </div>
                  </div>
                </article>
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
.message {
  display: flex;
  &__icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 16px;
    overflow: hidden;
  }
  &__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  &__info {
    margin-right: auto;
  }
  &__time {
    font-weight: 600;
    line-height: 150%;
  }
  &__not-read {
    margin-left: auto;
    background-color: rgb(246, 81, 96);;
    border: 2px solid rgb(255, 255, 255);
    width: max-content;
    border-radius: 50%;
    padding: 2px 4px;
  }
  &__text-count {
    color: rgb(255, 255, 255);
    font-size: 12px;
    font-weight: 600;
    line-height: 150%;
  }
}
</style>
