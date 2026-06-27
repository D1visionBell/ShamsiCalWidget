package com.shamsicalwidget.widget

import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.ComponentName
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.widget.RemoteViews
import com.shamsicalwidget.R
import com.shamsicalwidget.util.JalaliCalendar

class LockScreenWidgetProvider : AppWidgetProvider() {

    override fun onReceive(
        context: Context,
        intent: Intent
    ) {

        super.onReceive(context, intent)

        when (intent.action) {

            Intent.ACTION_DATE_CHANGED,
            Intent.ACTION_TIME_CHANGED,
            Intent.ACTION_TIMEZONE_CHANGED,
            AppWidgetManager.ACTION_APPWIDGET_UPDATE -> {

                val manager =
                    AppWidgetManager.getInstance(context)

                val ids =

                    manager.getAppWidgetIds(

                        ComponentName(

                            context,

                            LockScreenWidgetProvider::class.java

                        )

                    )

                onUpdate(

                    context,

                    manager,

                    ids

                )

            }

        }

    }

    override fun onUpdate(

        context: Context,

        appWidgetManager: AppWidgetManager,

        appWidgetIds: IntArray

    ) {

        WidgetUpdateService.scheduleDailyAlarm(context)

        appWidgetIds.forEach {

            updateWidget(

                context,

                appWidgetManager,

                it

            )

        }

    }

    override fun onEnabled(
        context: Context
    ) {

        super.onEnabled(context)

        WidgetUpdateService.scheduleDailyAlarm(
            context
        )

    }

    override fun onAppWidgetOptionsChanged(

        context: Context,

        appWidgetManager: AppWidgetManager,

        appWidgetId: Int,

        newOptions: Bundle

    ) {

        updateWidget(

            context,

            appWidgetManager,

            appWidgetId

        )

    }

    companion object {

        fun updateWidget(

            context: Context,

            appWidgetManager: AppWidgetManager,

            appWidgetId: Int

        ) {

            val jalali =
                JalaliCalendar.today()

            val views =

                RemoteViews(

                    context.packageName,

                    R.layout.widget_lock

                )

            views.setTextViewText(

                R.id.tv_lock_day_of_week,

                JalaliCalendar.dayName(

                    jalali.dayOfWeek

                )

            )

            views.setTextViewText(

                R.id.tv_lock_day_number,

                JalaliCalendar.toPersianDigits(

                    jalali.day

                )

            )

            views.setTextViewText(

                R.id.tv_lock_month,

                JalaliCalendar.monthName(

                    jalali.month

                )

            )

            val intent =
                Intent(Intent.ACTION_MAIN)

            intent.addCategory(

                Intent.CATEGORY_APP_CALENDAR

            )

            intent.flags =
                Intent.FLAG_ACTIVITY_NEW_TASK

            val pending =

                PendingIntent.getActivity(

                    context,

                    3,

                    intent,

                    PendingIntent.FLAG_UPDATE_CURRENT or
                            PendingIntent.FLAG_IMMUTABLE

                )

            views.setOnClickPendingIntent(

                R.id.widget_lock_root,

                pending

            )

            appWidgetManager.updateAppWidget(

                appWidgetId,

                views

            )

        }

    }

}
