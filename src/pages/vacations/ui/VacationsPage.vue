<template>
    <section class="projects-page">
        <HeaderPage />
        <div class="wrapper">
            <div class="projects-page__employees">
                <CardEmployee
                    :data="{
                        job: 'zu@pasajpot.org',
                        name: 'Samuel Curry',
                        isShowLine: true,
                        isBorderRound: true,
                        isShadow: true,
                    }"
                    v-for="index in 6"
                    :key="index"
                >
                    <template #content>
                        <div class="projects-page__info">
                            <div class="projects-page__column">
                                <div class="projects-page__title">
                                    From
                                </div>
                                <div class="projects-page__date">
                                    {{ new Date().getFullYear() }}
                                </div>
                            </div>
                            <div class="projects-page__column">
                                <div class="projects-page__title">
                                    To
                                </div>
                                <div class="projects-page__date">
                                    {{ new Date().getFullYear() }}
                                </div>
                            </div>
                            <div class="projects-page__column">
                                <div class="projects-page__title">
                                    Total
                                </div>
                                <div class="projects-page__date">
                                    {{ new Date().getDate() }}
                                </div>
                            </div>
                        </div>
                    </template>
                </CardEmployee>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue';
import { CardEmployee } from '@/entities/employee';
import { HeaderPage } from '@/entities/header-page';

useHead({
  title: 'Projects'
});

/* onBeforeUnmount(() => {
  bookModel.$reset()
}) */
</script>

<style lang="scss">
.projects-page {
  &__employees {
    display: flex;
    flex-direction: column;
    row-gap: 20px;
    margin-bottom: 50px;
  }
  &__info {
    display: flex;
    margin-top: 24px;
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
}
</style>
