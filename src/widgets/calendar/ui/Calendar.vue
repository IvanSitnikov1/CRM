<template>
    <div class="wrapper">
        <section class="calendar">
            <DataPiker
                :data="{
                    events: state.events,
                }"
            />
            <hr>
            <Title
                class="calendar__title"
                :data="{
                    title: 'September 18, 2020',
                    size: 'small',
                    isHighLeading: true,
                    marginBottom: 'medium',
                }"
            />

            <div class="calendar__events">
                <article
                    class="event-label calendar__event"
                    v-for="index in 4"
                    :key="index"
                >
                    <div class="event-label__content">
                        <Title
                            :data="{
                                title: 'Marc’s Birthday',
                                size: 'small',
                                isHighLeading: true,
                            }"
                        />
                        <div class="event-label__status">
                            <span class="event-label__time">2h</span>
                            <IconBase
                                :data="{
                                    iconName: 'arrowDown',
                                }"
                            />
                        </div>
                    </div>
                </article>
            </div>
        </section>
    </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import { DataPiker } from '@/shared/ui/data-picker';
import { Title } from '@/shared/ui/title';
import { IconBase } from '@/shared/ui/icon-base';
import { getEventForMonth } from '@/widgets/calendar/api';
import { TimePicker } from '@/shared/ui/time-picker';
import { BottomSheet } from '@/entities/bottom-sheet';

const router = useRouter();


const state = reactive({
  events: new Map()
});

onMounted(async () => {
  state.events = await getEventForMonth();
});
</script>

<style lang="scss">
  @import "style.module";

  .date-selector {
    display: flex;
    justify-content: space-between;
  }
</style>
