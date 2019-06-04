def addDaysToBundle(bundle):
    bundle.dropoff_month = 5
    bundle.dropoff_day = 29
    bundle.ready_month = 6
    bundle.ready_day = 2
    return bundle

def addPickupDays(bundle):
    bundle.dropoff_month = 5
    bundle.dropoff_day = 29
    bundle.ready_month = 6
    bundle.ready_day = 2
    bundle.pickup_month = 6
    bundle.pickup_day = 5
    return bundle
