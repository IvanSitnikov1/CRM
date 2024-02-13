<template>
  <section class="profile-page">
    <Header class="wrapper wrapper_title" :data="{
      title: 'Employee’s Profile'
    }"/>
    <div class="wrapper">
      <article class="about-user">
        <header class="about-user__header">
          <CircleProgressBar class="about-user__circle"
                             :data="{
                                size: 76,
                                value: 23,
                                max: 66,
                              }">
            <div class="about-user__avatar">
              <img class="about-user__image"
                   src="@/shared/assets/test.png"
                   alt="avatar">
            </div>
          </CircleProgressBar>
          <Title :data="{
          title: 'Gabriel Brown',
          isHighLeading: true,
        }"/>
          <span>UI/UX Designer</span>
        </header>
        <hr class="about-user__line">
        <main class="about-user__main">
          <div class="about-user__groups">
            <div class="about-user__group">
              <Title :data="{
                  title: 'Main info',
                  marginBottom: 'small'
                }"/>
              <div class="about-user__info">
                <UIInput :data="{
            value: 'UI/UX Designer',
            type: 'text',
            name: 'position',
            title: 'Position',
            isReadonly: true
          }"/>
                <UIInput :data="{
            value: 'Cadabra',
            type: 'text',
            name: 'company',
            title: 'Company',
            isReadonly: true
          }"/>
                <UIInput :data="{
            value: 'NYC, New York, USA',
            type: 'text',
            name: 'location',
            title: 'Location',
            isReadonly: true,
            iconName: 'Location'
          }">
                  <template #icon>
                    <ArrowRightIcon/>
                  </template>
                </UIInput>
                <UIInput :data="{
            value: 'May 19, 1996',
            type: 'text',
            name: 'birthday',
            title: 'Birthday Date',
            isReadonly: true,
            iconName: 'Birthday Date'
          }">
                  <template #icon>
                    <ArrowRightIcon/>
                  </template>
                </UIInput>
              </div>
            </div>
            <div class="about-user__group">
              <Title :data="{
                  title: 'Main info',
                  marginBottom: 'small'
                }"/>
              <div class="about-user__info">
                <UIInput :data="{
                    value: 'evanyates@gmail.com',
                    type: 'email',
                    name: 'email',
                    title: 'Email',
                    isReadonly: true
                  }"/>
                <UIInput :data="{
                    value: '+1 675 346 23-10',
                    type: 'tel',
                    name: 'tel',
                    title: 'Mobile Number',
                    isReadonly: true
                  }"/>
                <UIInput :data="{
                    value: 'Evan 2256',
                    type: 'text',
                    name: 'skype',
                    title: 'Skype',
                    isReadonly: true
                  }"/>
              </div>
            </div>
          </div>

        </main>
      </article>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { Header } from '@/shared/ui/header'
import { Title } from "@/shared/ui/title";
import { CircleProgressBar } from "@/shared/ui/circle-progress-bar";
import { UIInput } from "@/shared/ui/input";
import ArrowRightIcon from "@/shared/assets/icons/arrowRight.vue";

useHead({
  title: 'Profile'
})

</script>

<style lang="scss">
.about-user {
  border-radius: 24px;
  box-shadow: 0 6px 58px 0 rgba(196, 203, 214, 0.1);
  background: rgb(255, 255, 255);
  &__header {
    padding: 24px 20px;
  }
  &__avatar {
    height: 64px;
    width: 64px;
    border-radius: 50%;
    overflow: hidden;
  }
  &__line {
    margin: 0 0 24px;
  }
  &__info {
    display: flex;
    flex-direction: column;
    row-gap: 20px;
  }
  &__circle {
    width: max-content;
    margin-bottom: 16px;
  }
  &__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  &__main {
    padding: 0 20px 40px;
  }
  &__groups {
    display: flex;
    flex-direction: column;
    row-gap: 36px;
  }
}
</style>
