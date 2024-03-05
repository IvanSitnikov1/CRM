<template>
    <section class="project-detail-page">
        <div class="wrapper wrapper_title project-detail-page__back">
            <Link
                :data="{
                    title: 'Back to Projects',
                    to: '/projects',
                    iconLeft: 'arrowLeftLong',
                }"
            />
        </div>
        <Title
            class="wrapper wrapper_title"
            :data="{
                title: 'UX Login + Registration',
            }"
        />
        <div class="wrapper">
            <article class="project-description">
                <header class="project-description__header">
                    <Title
                        :data="{
                            title: 'Task info',
                            size: 'small',
                            isHighLeading: true,

                        }"
                    />
                </header>
                <main>
                    <div class="project-description__info">
                        <div class="project-description__reporter">
                            <span class="project-description__column-name">Reporter</span>
                            <TagUser
                                :data="{
                                    fullName: 'Blake Maxwell',
                                    image: '',
                                }"
                            />
                        </div>
                        <div class="project-description__assignees">
                            <span class="project-description__column-name">Assignees</span>
                            <Avatars :data="{}" />
                        </div>
                        <div class="project-description__priority">
                            <span class="project-description__column-name">Priority</span>
                            <Priority
                                :data="{
                                    priority: 'medium',
                                    isShowText: true,
                                }"
                            />
                        </div>
                        <div class="project-description__deadline">
                            <span class="project-description__column-name">Dead Line</span>
                            <time class="project-description__deadline-data">Feb 23, 2020</time>
                        </div>
                    </div>
                    <div class="project-description__time">
                        <Title
                            :data="{
                                title: 'Time tracing',
                                size: 'medium',
                                marginBottom: 'medium',
                                isHighLeading: true,
                            }"
                        />
                        <div class="project-description__log-time">
                            <CircleProgressBar
                                :data="{
                                    value: 12,
                                    max: 14,
                                    size: 40,
                                }"
                            />
                            <div class="project-description__text-time">
                                <Title
                                    :data="{
                                        title: '1d 3h 25m logged',
                                        size: 'small',
                                    }"
                                />
                                <span>Original Estimate 3d 8h</span>
                            </div>
                        </div>
                        <UiButton
                            :data="{
                                title: 'Log time',
                                type: 'button',
                                isFull: true,
                                iconNameLeft: 'clock',
                            }"
                        />
                    </div>

                    <div class="project-description__created">
                        <IconBase
                            :data="{
                                iconName: 'calendar',
                            }"
                        />
                        <time class="project-description__created-data">
                            Created May 28, 2020
                        </time>
                    </div>
                </main>
            </article>
        </div>
        <Title
            class="wrapper wrapper_title"
            :data="{
                title: 'Task Details',
            }"
        />
        <div class="wrapper">
            <article class="project-description">
                <header class="project-description__header">
                    <div>
                      in review
                    </div>
                    <ActionEdit />
                </header>
                <div class="project-description__number">
                <span class="project-description__title">Project Number</span>
                <span class="project-description__id">PN0001245</span>
              </div>
                <main>
                    <Title
                        :data="{
                            title: 'Description',
                            size: 'small',
                            marginBottom: 'small',
                            isHighLeading: true,
                        }"
                    />
                    <p class="project-description__description">
                        App for maintaining your medical record,
                        making appointments with a doctor, storing prescriptions
                    </p>
                    <div class="project-description__info">
                        <div class="project-description__reporter">
                            <span class="project-description__column-name">Reporter</span>
                            <TagUser
                                :data="{
                                    fullName: 'Blake Maxwell',
                                    image: '',
                                }"
                            />
                        </div>
                        <div class="project-description__assignees">
                            <span class="project-description__column-name">Assignees</span>
                            <Avatars :data="{}" />
                        </div>
                        <div class="project-description__priority">
                            <span class="project-description__column-name">Priority</span>
                            <Priority
                                :data="{
                                    priority: 'medium',
                                    isShowText: true,
                                }"
                            />
                        </div>
                        <div class="project-description__deadline">
                            <span class="project-description__column-name">Dead Line</span>
                            <time class="project-description__deadline-data">Feb 23, 2020</time>
                        </div>
                    </div>
                    <div class="project-description__created">
                        <IconBase
                            :data="{
                                iconName: 'calendar',
                            }"
                        />
                        <time class="project-description__created-data">
                            Created May 28, 2020
                        </time>
                    </div>
                </main>
                <footer class="project-description__footer">
                    <div class="project-description__actions">
                        <ActionAddFile />
                        <ActionCreatLink />
                    </div>
                </footer>
            </article>
        </div>
        <History />
    </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue';
import { Title } from '@/shared/ui/title';
import { Link } from '@/shared/ui/link';
import { IconBase } from '@/shared/ui/icon-base';
import { TagUser } from '@/shared/ui/tag-user';
import { Priority } from '@/shared/ui/priority';
import { ActionAddFile } from '@/features/add-file';
import { Avatars } from '@/shared/ui/avatars';
import { ActionCreatLink } from '@/features/creat-link';
import { ActionEdit } from '@/features/edit';
import { History } from '@/widgets/history';
import { CircleProgressBar } from '@/shared/ui/circle-progress-bar';
import { UiButton } from '@/shared/ui/button';

useHead({
  title: 'Project details'
});

</script>

<style lang="scss">
.project-detail-page {
  &__description {
    margin-bottom: 52px;
  }
}

.project-description {
  border-radius: 24px;
  box-shadow: 0 6px 58px 0 rgba(196, 203, 214, 0.1);
  background: rgb(255, 255, 255);
  padding: 24px;
  &__header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 28px;
  }
  &__number {
    display: flex;
    flex-direction: column;
    row-gap: 8px;
  }
  &__created {
    display: flex;
    column-gap: 8px;
    align-items: center;
    color: rgb(125, 133, 146);
    font-weight: 600;
  }
  &__time {
    border-radius: 14px;
    background: rgb(244, 249, 253);
    padding: 20px 24px;
    margin-bottom: 24px;
  }
  &__log-time {
    display: flex;
    align-items: center;
    column-gap: 20px;
    margin-bottom: 32px;
  }
  &__text-time {
    display: flex;
    flex-direction: column;
    row-gap: 4px;
  }
  &__id,
  &__description,
  &__deadline-data {
    color: rgb(10, 22, 41);
    font-size: 16px;
    line-height: 150%;
  }
  &__info {
    display: grid;
    grid-column-gap: 8px;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-row-gap: 24px;
    margin-bottom: 24px;
  }
  &__actions {
    display: flex;
    column-gap: 16px;
  }
  &__footer {
    margin-top: 32px;
  }
  &__column-name {
    display: block;
    margin-bottom: 8px;
  }
}

.edit {
  width: 44px;
  height: 44px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgb(244, 249, 253);
}
</style>
