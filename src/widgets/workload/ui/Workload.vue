<template>
    <div class="wrapper wrapper_big-margin">
        <section class="workload">
            <TitleWithLink
                :data="{
                    title: {
                        title: 'Workload',
                    },
                    link: {
                        title: 'View all',
                        to: '/employees',
                    },
                }"
            >
                <template #content>
                    <div class="workload__employees">
                        <Card
                            v-for="index in 6"
                            :key="index"
                            :data="{
                                isWhite: false,
                                isBox: false,
                                fullName: 'Shawn Stone',
                                tag: 'Middle',
                                job: 'UI/UX Designer',
                                image: 'https://cdn.tripster.ru/thumbs2/f5a8c1fe-b128-11ed-9e63-2e5ef03bee8d.1220x600.jpeg',
                            }"
                        />
                    </div>
                </template>
            </TitleWithLink>
        </section>
    </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { Card } from '@/entities/user';
import { TitleWithLink } from '@/entities/grop-title';

const router = useRouter();

const goToHome = () => {
  router.push({ path: '/' });
};

</script>

<style lang="scss">
  @import "style.module";
</style>
